from datetime import timedelta
import inspect
import os
import time
from uuid import uuid4

from fireworks._const import FIREWORKS_API_BASE_URL
from fireworks.evaluator.evaluator import Evaluator
from fireworks.llm._types import WandbConfigParam
from fireworks.reinforcement_fine_tuning_job.reinforcement_fine_tuning_job import ReinforcementFineTuningJob
from fireworks.client.api_client import FireworksClient
from functools import cache as sync_cache
from google.protobuf.field_mask_pb2 import FieldMask as SyncFieldMask
from typing import (
    Any,
    Callable,
    List,
    Optional,
    Union,
    TYPE_CHECKING,
)
from fireworks.dataset import Dataset
from fireworks.gateway import Gateway
from google.protobuf.duration_pb2 import Duration
from fireworks.control_plane.generated.protos_grpcio.gateway.deployment_pb2 import (
    Deployment as SyncDeployment,
    AutoscalingPolicy as SyncAutoscalingPolicy,
    AcceleratorType as SyncAcceleratorType,
    Region as SyncRegion,
    MultiRegion as SyncMultiRegion,
    DirectRouteType as SyncDirectRouteType,
    AutoTune as SyncAutoTune,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.model_pb2 import (
    Model as SyncModel,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.deployed_model_pb2 import (
    CreateDeployedModelRequest as SyncCreateDeployedModelRequest,
    DeployedModel as SyncDeployedModel,
    ListDeployedModelsRequest as SyncListDeployedModelsRequest,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.training_pb2 import (
    BaseTrainingConfig as SyncBaseTrainingConfig,
)
from fireworks.control_plane.generated.protos.gateway import (
    AcceleratorType as AcceleratorTypeEnum,
    AutoTune,
    AutoscalingPolicy,
    BaseTrainingConfig,
    Deployment,
    DeploymentState,
    InferenceParameters,
)
from fireworks._util import generate_model_resource_name, is_valid_resource_name
import sysconfig
from fireworks._literals import (
    DeploymentStrategyLiteral,
    DeploymentTypeLiteral,
    DirectRouteTypeLiteral,
    MultiRegionLiteral,
    PrecisionLiteral,
    RegionLiteral,
    AcceleratorTypeLiteral,
    WeightPrecisionLiteral,
)
from fireworks._logger import log_execution_time, logger
from fireworks.control_plane.generated.protos_grpcio.gateway.supervised_fine_tuning_job_pb2 import (
    SupervisedFineTuningJob as SyncSupervisedFineTuningJob,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.reinforcement_fine_tuning_job_pb2 import (
    ReinforcementFineTuningJob as SyncReinforcementFineTuningJob,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.training_pb2 import (
    BaseTrainingConfig as SyncBaseTrainingConfig,
    WeightPrecision,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.wandb_pb2 import (
    WandbConfig as SyncWandbConfig,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.batch_inference_job_pb2 import (
    InferenceParameters as SyncInferenceParameters,
)
from fireworks.llm.chat_completion import ChatCompletion, Chat
from fireworks.llm.completion import Completion
from fireworks.llm.metrics import Metrics
from fireworks.llm.responses import Responses

# Type checking imports to avoid circular imports
if TYPE_CHECKING:
    from fireworks.supervised_fine_tuning_job import SupervisedFineTuningJob

DEFAULT_MAX_RETRIES = 10
DEFAULT_DELAY = 0.5


class LLM:
    def __init__(
        self,
        model: str,
        deployment_type: DeploymentTypeLiteral,
        id: Optional[str] = None,
        deployment_display_name: Optional[str] = None,
        base_id: Optional[str] = None,
        api_key: Optional[str] = None,
        direct_route_api_key: Optional[str] = None,
        base_url: str = f"{FIREWORKS_API_BASE_URL}/inference/v1",
        max_retries: int = DEFAULT_MAX_RETRIES,
        request_timeout: int = 600,
        scale_up_window: timedelta = timedelta(seconds=1),
        scale_down_window: timedelta = timedelta(minutes=1),
        scale_to_zero_window: timedelta = timedelta(minutes=5),
        enable_metrics: bool = False,
        accelerator_type: Optional[AcceleratorTypeLiteral] = None,
        region: Optional[RegionLiteral] = None,
        multi_region: Optional[MultiRegionLiteral] = None,
        description: Optional[str] = None,
        annotations: Optional[dict[str, str]] = None,
        min_replica_count: Optional[int] = None,
        max_replica_count: Optional[int] = None,
        replica_count: Optional[int] = None,
        accelerator_count: Optional[int] = None,
        precision: Optional[PrecisionLiteral] = None,
        world_size: Optional[int] = None,
        generator_count: Optional[int] = None,
        disaggregated_prefill_count: Optional[int] = None,
        disaggregated_prefill_world_size: Optional[int] = None,
        max_batch_size: Optional[int] = None,
        cluster: Optional[str] = None,
        enable_addons: Optional[bool] = None,
        draft_token_count: Optional[int] = None,
        draft_model: Optional[str] = None,
        ngram_speculation_length: Optional[int] = None,
        max_peft_batch_size: Optional[int] = None,
        kv_cache_memory_pct: Optional[int] = None,
        enable_session_affinity: Optional[bool] = None,
        direct_route_api_keys: Optional[list[str]] = None,
        num_peft_device_cached: Optional[int] = None,
        direct_route_type: Optional[DirectRouteTypeLiteral] = None,
        direct_route_handle: Optional[str] = None,
        long_prompt_optimized: Optional[bool] = None,
        temperature: Optional[float] = None,
        perf_metrics_in_response: Optional[bool] = None,
        max_connections: Optional[int] = None,
        client_kwargs: dict[str, Any] = {},
    ):
        """
        Initialize an LLM object. Performs validation of the model and deployment type.

        Args:
            model: The model to use.
            deployment_type: The deployment type to use. Must be one of
                "serverless", "on-demand", "auto", or "on-demand-lora". For experimentation on
                quality, we recommend using "auto" to default to the most
                cost-effective option. If you plan to run large evaluation jobs or
                have workloads that would benefit from dedicated resources, we
                recommend using "on-demand". Otherwise, you can enforce that you
                only use "serverless" by setting this parameter to "serverless".
            id: The id of the deployment to use. This is required when deployment_type is "on-demand".
            base_id: The base deployment id to use. This is required when deployment_type is "on-demand-lora".
            deployment_display_name: The display name of the deployment to use.
                If not provided, the deployment display name will be generated
                from the filename of the caller where this LLM was instantiated.
            api_key: The API key to use.
            direct_route_api_key: The API key to use for direct route.
            base_url: The base URL to use.
            accelerator_type: The accelerator type to use.
            scale_up_window: The scale up window to use.
            scale_down_window: The scale down window to use.
            scale_to_zero_window: The scale to zero window to use.
            enable_metrics: Whether to enable metrics. Only records time to last token for non-streaming requests.
            max_retries: The maximum number of retries to use.
            max_connections: The maximum number of concurrent connections to configure for the FireworksClient.
            client_kwargs: Additional keyword arguments to pass to the FireworksClient.
            For more information on parameters, see the [API Reference](https://docs.fireworks.ai/api-reference/post-chatcompletions)
        """
        if not model:
            raise ValueError("model is required")
        if deployment_type is None:
            raise ValueError('deployment_type is required - must be one of "serverless", "on-demand", or "auto"')
        self._direct_route_api_key = direct_route_api_key
        self._client = FireworksClient(
            request_timeout=request_timeout,
            api_key=direct_route_api_key if self.direct_route_api_key else api_key,
            base_url=base_url,
            max_connections=max_connections,
            **client_kwargs,
        )
        self._id = id
        self._gateway = Gateway(api_key=api_key)
        self._deployment_display_name = deployment_display_name
        self._direct_route_api_key = direct_route_api_key
        self._ran_setup = False
        self._model = model
        if base_id is not None and not self.is_peft_addon():
            raise ValueError("base_id is only for PEFT addons. Use id instead for specifying an existing deployment.")
        self._base_id = base_id
        self.chat = Chat(self, self.model)
        self.completions = Completion(self)
        self.max_retries = max_retries
        self.responses = Responses(self)
        self.deployment_type: DeploymentTypeLiteral = deployment_type
        self.deployment_strategy = self._compute_deployment_strategy()
        if self.deployment_strategy == "on-demand":
            if id is None:
                raise ValueError("LLM(id=...) must be provided when deployment_strategy is on-demand")
            if id == "":
                raise ValueError("LLM(id=...) must not be empty when deployment_strategy is on-demand")
        if self.deployment_strategy == "on-demand-lora":
            if id is not None:
                raise ValueError(
                    "LLM(id=...) must not be provided when deployment_strategy is on-demand-lora. Fireworks automatically generates an ID when loading a LoRA."
                )
            if base_id is None:
                raise ValueError("LLM(base_id=...) must be provided when deployment_strategy is on-demand-lora")
            if base_id == "":
                raise ValueError("LLM(base_id=...) must not be empty when deployment_strategy is on-demand-lora")
        self.enable_metrics = enable_metrics
        self._metrics = Metrics()

        # This needs to be run in __init__ to ensure we capture deployment name
        # inside of this thread
        self._get_deployment_display_name()

        self._accelerator_type_original: Optional[AcceleratorTypeLiteral] = accelerator_type
        if isinstance(accelerator_type, str):
            self._accelerator_type = AcceleratorTypeEnum.from_string(accelerator_type)
            self._validate_model_for_gpu(self.model, self._accelerator_type)
            self._accelerator_type_sync: Optional[SyncAcceleratorType] = getattr(SyncAcceleratorType, accelerator_type)
        else:
            self._accelerator_type = accelerator_type
            self._accelerator_type_sync = accelerator_type

        # aggressive defaults for experimentation to save on cost
        self._autoscaling_policy: AutoscalingPolicy = AutoscalingPolicy(
            scale_up_window=scale_up_window,
            scale_down_window=scale_down_window,
            scale_to_zero_window=scale_to_zero_window,
        )
        self._autoscaling_policy_sync = SyncAutoscalingPolicy(
            scale_up_window=Duration(seconds=int(scale_up_window.total_seconds())),
            scale_down_window=Duration(seconds=int(scale_down_window.total_seconds())),
            scale_to_zero_window=Duration(seconds=int(scale_to_zero_window.total_seconds())),
        )
        self._region: Optional[RegionLiteral] = region
        self._multi_region: Optional[MultiRegionLiteral] = multi_region
        self._description = description
        self._annotations = annotations
        self._min_replica_count = min_replica_count
        self._max_replica_count = max_replica_count
        self._replica_count = replica_count
        self._accelerator_count = accelerator_count
        self._precision: Optional[PrecisionLiteral] = precision
        self._world_size = world_size
        self._generator_count = generator_count
        self._disaggregated_prefill_count = disaggregated_prefill_count
        self._disaggregated_prefill_world_size = disaggregated_prefill_world_size
        self._max_batch_size = max_batch_size
        self._cluster = cluster
        self._enable_addons = enable_addons
        self._draft_token_count = draft_token_count
        self._draft_model = draft_model
        self._ngram_speculation_length = ngram_speculation_length
        self._max_peft_batch_size = max_peft_batch_size
        self._kv_cache_memory_pct = kv_cache_memory_pct
        self._enable_session_affinity = enable_session_affinity
        self._direct_route_api_keys = direct_route_api_keys
        self._num_peft_device_cached = num_peft_device_cached
        self._direct_route_type: Optional[DirectRouteTypeLiteral] = direct_route_type
        self._direct_route_handle = direct_route_handle
        self._temperature = temperature
        self._perf_metrics_in_response = perf_metrics_in_response
        self._auto_tune = AutoTune()
        self._auto_tune_sync = SyncAutoTune()
        if long_prompt_optimized is not None:
            self._auto_tune.long_prompt_optimized = long_prompt_optimized
            self._auto_tune_sync.long_prompt = long_prompt_optimized

        if not self.is_available_on_serverless() and self.deployment_type == "serverless":
            raise ValueError(
                f"Model {self.model} is not available on serverless, but deployment_type is serverless, please use deployment_type='auto' or 'on-demand'"
            )

    @property
    def direct_route_api_key(self) -> Optional[str]:
        return self._direct_route_api_key

    @property
    def deployment_id(self) -> Optional[str]:
        # accounts/<account_id>/deployments/<deployment_id>
        return self._id

    @property
    def deployment_name(self) -> Optional[str]:
        """
        Properly converts provided deployment name to a full resource name if
        only the ID was provided.

        If this model is a PEFT addon, the deployment name will be the deployed model name.

        NOTE: Does not query the API to get the full resource name if deployment
        name was not provided on instantiation.
        """
        if self._id is None:
            return None
        if self._id.startswith("accounts/"):
            return self._id
        if (
            self.is_peft_addon()
            and self.deployment_strategy == "on-demand-lora"
            or self.deployment_strategy == "serverless-lora"
        ):
            return f"accounts/{self._gateway.account_id()}/deployedModels/{self._id}"
        return f"accounts/{self._gateway.account_id()}/deployments/{self._id}"

    @property
    def base_deployment_id(self) -> Optional[str]:
        # accounts/<account_id>/deployments/<base_deployment_id>
        return self._base_id

    @property
    def base_deployment_name(self):
        """
        Used for on-demand-lora deployments.

        The base deployment name to use. If not provided, the base deployment
        name will be queried by looking for base models with the same display
        name. Display names are generated from file names or provided explicitly
        through deployment_display_name. This is useful when you want to specify
        a base deployment for LoRA addons.
        """
        if self._base_id is None:
            return None
        if self._base_id.startswith("accounts/"):
            return self._base_id
        return f"accounts/{self._gateway.account_id()}/deployments/{self._base_id}"

    @property
    def temperature(self):
        return self._temperature

    @property
    def perf_metrics_in_response(self):
        return self._perf_metrics_in_response

    @property
    def model(self):
        if not self._model.startswith("accounts/fireworks/models/") and "/" not in self._model:
            model = f"accounts/fireworks/models/{self._model}"
            if self.is_model_on_fireworks_account(model):
                return model
        if not self._model.startswith("accounts/"):
            account_id = self._gateway.account_id()
            return f"accounts/{account_id}/models/{self._model}"
        return self._model

    @staticmethod
    def _validate_model_for_gpu(model: str, accelerator_type: AcceleratorTypeEnum):
        """
        Models are not always supported on all GPU types. This function checks if the model is supported on a GPU.
        """
        if "qwen3-1p7b" in model:
            supported_accelerators = [
                AcceleratorTypeEnum.NVIDIA_H100_80GB,
                AcceleratorTypeEnum.NVIDIA_H200_141GB,
            ]
            if accelerator_type not in supported_accelerators:
                raise ValueError(
                    f"Qwen3-1p7b is not supported on {accelerator_type}. "
                    f"Please pass one of the following accelerators: {list(map(str, supported_accelerators))} "
                    f"to the LLM constructor using the accelerator_type parameter.\n\n"
                    f"Example:\n"
                    f"    from fireworks import LLM\n"
                    f"    llm = LLM(\n"
                    f'        model="qwen3-1p7b",\n'
                    f'        accelerator_type="NVIDIA_H100_80GB"\n'
                    f"    )"
                )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._gateway.__aexit__(exc_type, exc_val, exc_tb)

    @property
    def deployment_display_name(self) -> str:
        """
        IMPORTANT: This is used to identify a deployment in the SDK.

        This is the name that will be used to display the deployment in the UI.

        Not sure if we should really be using deployment name for querying
        existing deployments but this way we don't have to worry about name
        collisions since display name is not a unique identifier for
        deployments. Name collisions are important to avoid because you might
        want to have multiple deployments with different parameters in the same
        file/notebook/namespace. So display name is really treated like a
        namespace.
        """
        return self._get_deployment_display_name()

    @sync_cache
    def _get_deployment_display_name(self):
        """
        If a name was specified, deployment name will be the specified name.
        Otherwise, the deployment name will be generated from the filename of the caller where this LLM was instantiated.

        In Jupyter notebooks, we'll use the actual notebook filename rather than the temporary execution file.

        For serverless models, deployment display name is not required since no deployment is created,
        so we return a default name if caller context cannot be determined.
        """
        if self._deployment_display_name is not None:
            return self._deployment_display_name

        # Check if running in a Jupyter notebook environment
        try:
            # Check for Jupyter environment via environment variable
            notebook_path = os.environ.get("JPY_SESSION_NAME")

            if notebook_path:
                logger.debug(f"Found notebook path from environment: {notebook_path}")
                notebook_filename = os.path.basename(notebook_path)
                logger.debug(f"Extracted notebook filename: {notebook_filename}")
                return notebook_filename
        except Exception as e:
            logger.debug(f"Error getting notebook name from environment: {str(e)}")
            pass

        # Get fireworks package path and Python stdlib path
        import fireworks

        package_path = os.path.dirname(fireworks.__file__)
        stdlib_path = sysconfig.get_path("stdlib")

        stack = inspect.stack()
        for frame_info in stack:
            filename = frame_info.filename
            # Skip frames from our package, Python stdlib, other libraries, and internal Python
            if (
                not filename.startswith(package_path)
                and not filename.startswith(stdlib_path)
                and not "/site-packages/" in filename
                and not filename.startswith("<")
            ):
                logger.debug(f"Found caller outside of library code to generate name: {filename}")
                return os.path.basename(filename)

        # If no caller found, we assume this is a REPL session and return a default name
        return "repl-session"

    def apply(self, wait: bool = True):
        """
        Like Terraform apply, this will ensure the deployment is ready and return the deployment.
        """
        self._ensure_deployment_ready(wait=wait)
        return self

    def _with_modified_params(self, **kwargs) -> "LLM":
        """
        Helper method to create a new LLM instance with modified parameters.

        Args:
            **kwargs: Parameters to override in the new LLM instance

        Returns:
            A new LLM instance with the specified parameters modified
        """
        # Try to get api_key and base_url from the client
        api_key = self._client.api_key
        base_url = self._client.base_url
        # Get long_prompt_optimized if it exists
        long_prompt_optimized = getattr(self._auto_tune, "long_prompt_optimized", None)

        # Default parameters from current instance
        params = {
            "model": self._model,
            "deployment_type": self.deployment_type,
            "id": self._id,
            "deployment_display_name": self._deployment_display_name,
            "api_key": api_key,
            "base_url": str(base_url),
            "max_retries": self.max_retries,
            "accelerator_type": self._accelerator_type_original,
            "scale_up_window": self._autoscaling_policy.scale_up_window,
            "scale_down_window": self._autoscaling_policy.scale_down_window,
            "scale_to_zero_window": self._autoscaling_policy.scale_to_zero_window,
            "enable_metrics": self.enable_metrics,
            "region": self._region,
            "description": self._description,
            "annotations": self._annotations,
            "min_replica_count": self._min_replica_count,
            "max_replica_count": self._max_replica_count,
            "replica_count": self._replica_count,
            "accelerator_count": self._accelerator_count,
            "precision": self._precision,
            "world_size": self._world_size,
            "generator_count": self._generator_count,
            "disaggregated_prefill_count": self._disaggregated_prefill_count,
            "disaggregated_prefill_world_size": self._disaggregated_prefill_world_size,
            "max_batch_size": self._max_batch_size,
            "cluster": self._cluster,
            "enable_addons": self._enable_addons,
            "draft_token_count": self._draft_token_count,
            "draft_model": self._draft_model,
            "ngram_speculation_length": self._ngram_speculation_length,
            "max_peft_batch_size": self._max_peft_batch_size,
            "kv_cache_memory_pct": self._kv_cache_memory_pct,
            "enable_session_affinity": self._enable_session_affinity,
            "direct_route_api_keys": self._direct_route_api_keys,
            "num_peft_device_cached": self._num_peft_device_cached,
            "direct_route_type": self._direct_route_type,
            "direct_route_handle": self._direct_route_handle,
            "long_prompt_optimized": long_prompt_optimized,
            "temperature": self._temperature,
            "perf_metrics_in_response": self._perf_metrics_in_response,
        }

        # Override with provided parameters
        params.update(kwargs)

        return LLM(**params)

    def with_deployment_type(self, deployment_type: DeploymentTypeLiteral) -> "LLM":
        """
        Returns a new LLM with the deployment type set to the given value.
        """
        return self._with_modified_params(deployment_type=deployment_type)

    def with_temperature(self, temperature: Optional[float]) -> "LLM":
        """
        Returns a new LLM with the temperature set to the given value.
        """
        return self._with_modified_params(temperature=temperature)

    def with_perf_metrics_in_response(self, perf_metrics_in_response: Optional[bool]) -> "LLM":
        """
        Returns a new LLM with the perf_metrics_in_response set to the given value.
        """
        return self._with_modified_params(perf_metrics_in_response=perf_metrics_in_response)

    def get_time_to_last_token_mean(self) -> Optional[float]:
        """
        Returns the mean time to last token for non-streaming requests. If no metrics are available, returns None.
        """
        if not self.enable_metrics:
            raise ValueError("Metrics are not enabled for this LLM")
        return self._metrics.get_metric_mean("time_to_last_token")

    def is_available_on_serverless(self):
        """
        Checks if the model is available on serverless.
        """
        return self.is_model_available_on_serverless(self.model)

    def delete_deployment(self, ignore_checks: bool = False, wait: bool = True):
        """
        If there is an existing deployment, delete it.
        """
        deployment = self.get_deployment()
        if deployment is None:
            logger.debug("No deployment found to delete")
            return
        if self.is_peft_addon():
            if not isinstance(deployment, SyncDeployedModel):
                raise ValueError(f"Deployment {deployment.name} is not a deployed model")
            if deployment.state == SyncDeployedModel.State.UNDEPLOYING:
                logger.debug(f"LoRA model {self.model} is already unloading, skipping unloading request")
            else:
                if deployment.state == SyncDeployedModel.State.DEPLOYING:
                    logger.debug(
                        f"LoRA model {self.model} is already deploying, waiting for it to be deployed to delete it"
                    )
                    # we need to wait until the deployment is ready to delete it by waiting for it to be deployed
                    self.apply()
                logger.debug(f"Unloading LoRA model {self.model}, deployment={deployment.name}")
                self._gateway.delete_deployed_model_sync(deployment.name)
            if not wait:
                logger.debug(
                    f"wait=False, not polling for LoRA model unloading completion of deployment {deployment.name}"
                )
                return

            logger.debug(f"Unloading LoRA model {self.model}...")
            start_time = time.time()
            last_log_time = 0

            while True:
                current_time = time.time()

                # Try to get the deployed model to check if it still exists
                deployed_model = self._gateway.get_deployed_model_sync(deployment.name)

                if deployed_model is None:
                    # Deployed model no longer exists, deletion is complete
                    total_time = time.time() - start_time
                    logger.debug(f"Serverless LoRA model {self.model} deleted successfully!")
                    logger.debug(f"Deletion completed in {total_time:.2f} seconds!")
                    logger.debug(f"Deployed model {deployment.name} no longer exists (deleted successfully)")
                    break

                # Log detailed info every 10 seconds
                if current_time - last_log_time >= 10:
                    elapsed_so_far = current_time - start_time
                    state_name = SyncDeployedModel.State.Name(deployed_model.state)
                    logger.debug(
                        f"Waiting for deployed model {deployed_model.name} to be deleted, "
                        f"current state: {state_name}, elapsed time: {elapsed_so_far:.2f}s"
                    )
                    last_log_time = current_time

                # Wait before checking again
                time.sleep(2)

            return
        else:
            if not wait:
                logger.debug(f"wait=False, not polling for deployment deletion completion of {deployment.name}")
                return

            logger.debug(f"Deleting deployment {deployment.name}")
            # hard=True so we can reuse the same deployment ID
            self._gateway.delete_deployment_sync(deployment.name, ignore_checks, hard=True)
            # spin until deployment is deleted
            start_time = time.time()
            while deployment is not None:
                current_time = time.time()
                if current_time - start_time >= 10:
                    logger.debug(f"Waiting for deployment {deployment.name} to be deleted...")
                    start_time = current_time
                deployment = self.get_deployment()
                time.sleep(1)

    def _compute_deployment_strategy(self) -> DeploymentStrategyLiteral:
        """
        Determine whether to use serverless or dedicated deployment based on
        model availability, configured deployment type, and model type.

        Returns:
            DeploymentStrategyLiteral: The deployment strategy to use.
        """
        logger.debug(
            f"Computing deployment strategy for model {self.model} with deployment_type {self.deployment_type}"
        )

        if self.is_available_on_serverless():
            if self.deployment_type == "serverless" or self.deployment_type == "auto":
                logger.debug(f"Model {self.model} is available on serverless, using serverless deployment")
                return "serverless"
            else:
                logger.debug(
                    f"Model {self.model} is available on serverless, but deployment_type is on-demand, continuing to ensure deployment is ready"
                )
                return "on-demand"
        else:
            # Check if model supports serverless deployment
            if self.deployment_type in ["serverless", "auto", "on-demand-lora"] and self.is_peft_addon():
                if self.deployment_type == "on-demand-lora":
                    logger.debug(f"Model {self.model} is a PEFT model, using on-demand-lora deployment")
                    return "on-demand-lora"
                logger.debug(f"Checking if model {self.model} supports serverless LoRA")

                # If model supports serverless LoRA, use serverless deployment
                if self.supports_serverless_lora():
                    logger.debug(f"Model {self.model} supports serverless LoRA, using serverless deployment")
                    return "serverless-lora"

                # If deployment type is explicitly serverless but model doesn't support it, raise error
                if self.deployment_type == "serverless":
                    raise ValueError(
                        f"Model {self.model} is not Serverless LoRA enabled and deployment_type is serverless. "
                        f'Use deployment_type of "auto" or "on-demand" instead to deploy this LoRA onto an on-demand deployment.'
                    )

                if self.deployment_type == "auto":
                    """
                    If the model is not available on serverless, but the deployment type is auto,
                    we will deploy the base model with addons enabled, and load the LoRA onto it.
                    This is useful for models that are not available on serverless, but only want to use a single deployment
                    to save on GPU costs. If you really want dedicated resources, then use deployment_type="on-demand".
                    """
                    return "on-demand-lora"

            # Default to on-demand deployment if model is not available on serverless
            logger.debug(
                f"Model {self.model} is not available on serverless, continuing to check for existing deployment"
            )
            return "on-demand"

    def is_model_on_fireworks_account(self, model: str) -> Optional[SyncModel]:
        """
        Check if the model is on the fireworks account.
        If it is, return the model object.
        If it is not, return None.
        """
        models = self.list_fireworks_models()
        model_obj = next((m for m in models if m.name == model), None)
        return model_obj

    @sync_cache
    def is_model_available_on_serverless(self, model: str) -> bool:
        logger.debug(f"Checking if {model} is available on serverless")
        model_obj = self.is_model_on_fireworks_account(model)
        if model_obj is None:
            return False
        logger.debug(f"Found model {model} on under fireworks account")
        is_serverless = self.is_model_deployed_on_serverless_account(model_obj)
        logger.debug(f"Model {model} is {'serverless' if is_serverless else 'not serverless'}")
        return is_serverless

    @sync_cache
    def list_fireworks_models(self) -> List[SyncModel]:
        """
        Find all models on the fireworks account. Does not change often, so we
        embed the Gateway response as a variable in another file and return that
        instead. See the comment on what query is used to get the models.
        """
        result = []
        page_token = None
        while True:
            response = self._gateway.list_models_sync(
                parent=f"accounts/fireworks",
                page_size=200,
                page_token=page_token if page_token else "",
                include_deployed_model_refs=True,
            )
            result.extend(response.models)

            if not response.next_page_token:
                break
            page_token = response.next_page_token

        return result

    def is_model_deployed_on_serverless_account(self, model: SyncModel) -> bool:
        """
        Check if the model is deployed on a serverless-enabled account.

        Args:
            model: The model object to check

        Returns:
            bool: True if the model is deployed on a supported serverless account, False otherwise
        """
        if model.deployed_model_refs:
            for ref in model.deployed_model_refs:
                if (
                    hasattr(ref, "state")
                    and (ref.state == SyncDeployedModel.State.DEPLOYED or ref.state == "DEPLOYED")
                    and hasattr(ref, "deployment")
                    and ref.deployment
                ):
                    # Check if deployment is on a supported account
                    if (
                        ref.deployment.startswith("accounts/fireworks/")
                        or ref.deployment.startswith("accounts/yi-01-ai/")
                        or ref.deployment.startswith("accounts/sentientfoundation/")
                    ):
                        return True
        return False

    @log_execution_time
    def get_deployment(self) -> Optional[Union[SyncDeployment, SyncDeployedModel]]:
        """
        1. If a deployment ID is provided, return the deployment with that name.
        2. If deployment with that ID does not exist, return None.
        3. If model is a PEFT model and is not using live merge, return and deployed model with the same model
        4. Otherwise, look for deployment by model and display name
        """
        if self.is_peft_addon() and (
            self.deployment_strategy == "on-demand-lora" or self.deployment_strategy == "serverless-lora"
        ):
            if self.deployment_name is not None:
                deployed_model = self._gateway.get_deployed_model_sync(self.deployment_name)
                if deployed_model is None:
                    return None
                if deployed_model.model != self.model:
                    raise ValueError(f"Deployed model {self.deployment_name} is not for model {self.model}")
                return deployed_model
            request = SyncListDeployedModelsRequest(filter=f'model="{self.model}"')
            deployed_models = self._gateway.list_deployed_models_sync(request)
            deployed_model = next(iter(deployed_models.deployed_models), None)
            if deployed_model is None:
                return None
            return deployed_model

        if self.deployment_name is not None:
            deployment = self._gateway.get_deployment_sync(self.deployment_name)
            if deployment is None:
                return None
            if deployment.base_model != self.model:
                raise ValueError(f"Deployment {self.deployment_name} is not for model {self.model}")
            return deployment
        deployments = self._gateway.list_deployments_sync(
            filter=f'display_name="{self.deployment_display_name}" AND base_model="{self.model}"'
        )
        deployment = next(iter(deployments), None)
        return deployment

    def supports_serverless_lora(self) -> bool:
        loras = self._gateway.list_serverless_lora_sync()
        if self.peft_base_model is None:
            return False
        base_model_supported = any(lora_model == self.peft_base_model for lora_model in loras.models)
        if not base_model_supported:
            return False
        is_base_model_serverless = self.is_model_available_on_serverless(self.peft_base_model)
        if not is_base_model_serverless:
            return False
        return True

    @log_execution_time
    def _ensure_deployment_ready(self, wait: bool = True) -> None:
        """
        Ensure this LLM is deployed in any way, otherwise raise an error if it
        can't be deployed based on the deployment_type.
        """
        if self.deployment_strategy == "serverless":
            # no deployment needed, just return
            return
        deployment = self.get_deployment()
        if self.deployment_strategy == "serverless-lora":
            if deployment is not None:
                deployed_model = deployment
            else:
                request = SyncCreateDeployedModelRequest()
                request.deployed_model.display_name = self.deployment_display_name
                request.deployed_model.model = self.model
                deployed_model = self._gateway.create_deployed_model_sync(request)

            if deployed_model.state == SyncDeployedModel.State.DEPLOYED:
                return

            logger.debug(f"Deploying serverless LoRA model {self.model}...")

            if not wait:
                logger.debug(f"wait=False, not polling for deployment completion of {deployed_model.name}")
                return

            start_time = time.time()
            last_log_time = 0

            while deployed_model.state != SyncDeployedModel.State.DEPLOYED:
                current_time = time.time()

                # Log detailed info every 10 seconds
                if current_time - last_log_time >= 10:
                    elapsed_so_far = current_time - start_time
                    state_name = SyncDeployedModel.State.Name(deployed_model.state)
                    logger.debug(
                        f"Waiting for deployed model {deployed_model.name} to be ready, "
                        f"current state: {state_name}, elapsed time: {elapsed_so_far:.2f}s"
                    )
                    last_log_time = current_time

                # Check if deployment failed
                if deployed_model.state == SyncDeployedModel.State.STATE_UNSPECIFIED:
                    raise ValueError(f"Deployed model {deployed_model.name} failed to deploy")

                # Wait before checking again
                time.sleep(2)

                # Get updated deployed model state
                updated_deployed_model = self._gateway.get_deployed_model_sync(deployed_model.name)
                if updated_deployed_model is None:
                    raise ValueError(
                        f"Deployed model {deployed_model.name} was unexpectedly deleted during deployment"
                    )
                deployed_model = updated_deployed_model

            total_time = time.time() - start_time
            logger.debug(f"✅ Serverless LoRA model {self.model} deployed successfully!")
            logger.debug(f"✅ Deployment completed in {total_time:.2f} seconds!")
        elif self.deployment_strategy == "on-demand-lora":
            # Validate that a base model is specified for LoRA deployment
            if self.peft_base_model is None:
                raise ValueError(f"PEFT base model is not set for {self.model}")

            # Handle existing deployment if one exists
            if deployment is not None:
                logger.debug(f"Found existing deployment {deployment.name}")

                # Ensure the deployment is a deployed model, not a deployment
                if isinstance(deployment, SyncDeployment):
                    logger.debug(f"Deployment {deployment.name} is a deployment, not a deployed model")
                    raise ValueError(f"Deployment {deployment.name} is a deployment, not a deployed model")

                # Verify the deployment is for the correct model
                if deployment.model != self.model:
                    logger.debug(
                        f"Deployment {deployment.name} model {deployment.model} does not match expected model {self.model}"
                    )
                    raise ValueError(f"Existing deployment with name {deployment.name} is not for model {self.model}")

                # Validate base deployment name matches if specified
                if self.base_deployment_name is not None and deployment.deployment != self.base_deployment_name:
                    logger.debug(
                        f"Deployment {deployment.name} base deployment {deployment.deployment} "
                        f"does not match specified base deployment {self.base_deployment_name}"
                    )
                    raise ValueError(
                        f"Existing deployment with base deployment {deployment.name} "
                        f"does not match the provided base deployment name "
                        f"{self.base_deployment_name}. You should probably just use "
                        f"the existing deployment instead of creating a new one by "
                        f"removing base_deployment_name from LLM instantiation."
                    )

                if deployment.display_name != self.deployment_display_name:
                    logger.debug(
                        f'Deployment "{deployment.name}" has display name '
                        f'"{deployment.display_name}", but "{self.deployment_display_name}" '
                        f"was expected. Will reuse existing deployment as there is no "
                        f"functional difference in creating a new deployment"
                    )

                # Skip deployment if already successfully deployed
                if deployment.state == SyncDeployedModel.State.DEPLOYED:
                    logger.debug(f"Deployment {deployment.name} is already deployed, skipping")
                    return

                # Clean up failed deployments
                if deployment.state == SyncDeployedModel.State.UNDEPLOYING:
                    logger.debug(
                        f"Deployment {deployment.name} is in {SyncDeployment.State.Name(deployment.state)} state, deleting it"
                    )

                    # NOTE: does not respect `wait` argument since we need to
                    # actually wait until the deployed model is unloaded to
                    # trigger a create deployment call
                    self.delete_deployment()

                    logger.debug(f"Successfully deleted failed deployment {deployment.name}")
                    deployment = self.get_deployment()
                    assert deployment is None

            # Deploy the base model first with addons enabled
            base_model_llm = LLM(
                deployment_type="on-demand",
                enable_addons=True,
                model=self.peft_base_model,
                id=self.base_deployment_id,
                min_replica_count=self._min_replica_count,
                max_replica_count=self._max_replica_count,
                replica_count=self._replica_count,
                accelerator_count=self._accelerator_count,
                world_size=self._world_size,
                generator_count=self._generator_count,
                region=self._region,
                annotations=self._annotations,
                description=self._description,
            )
            base_model_llm.apply(wait=wait)
            base_model_deployment = base_model_llm.get_deployment()

            # Verify base model deployment was successful
            if base_model_deployment is None:
                raise ValueError(f"Base model {self.peft_base_model} is not deployed")

            if deployment is not None and deployment.state == SyncDeployedModel.State.DEPLOYING:
                logger.debug(f"LoRA model {self.model} is already deploying, skipping deployment")
                deployed_model = deployment
            else:
                # Create and deploy the LoRA model on top of the base model
                request = SyncCreateDeployedModelRequest()
                request.deployed_model.display_name = self.deployment_display_name
                request.deployed_model.model = self.model
                request.deployed_model.deployment = base_model_deployment.name
                deployed_model = self._gateway.create_deployed_model_sync(request)

            # Monitor the LoRA model deployment progress
            logger.debug(f"Loading LoRA model {self.model} onto base model deployment {base_model_deployment.name}")

            if not wait:
                logger.debug(f"wait=False, not polling for LoRA model loading completion of {deployed_model.name}")
                return

            start_time = time.time()
            last_log_time = 0

            while True:
                current_time = time.time()

                # Poll for deployment status
                deployed_model = self._gateway.get_deployed_model_sync(deployed_model.name)

                # Handle unexpected deletion during deployment
                if deployed_model is None:
                    raise ValueError(
                        f"Deployed model {request.deployed_model.name} was unexpectedly deleted during deployment"
                    )

                # Exit loop when deployment is successful
                if deployed_model.state == SyncDeployedModel.State.DEPLOYED:
                    total_time = time.time() - start_time
                    logger.debug(f"LoRA model {self.model} loaded successfully!")
                    logger.debug(f"Loading completed in {total_time:.2f} seconds!")
                    break

                # Handle deployment failure
                if deployed_model.state == SyncDeployedModel.State.STATE_UNSPECIFIED:
                    raise ValueError(f"Deployed model {deployed_model.name} failed to deploy")

                # Log progress every 10 seconds
                if current_time - last_log_time >= 10:
                    elapsed_so_far = current_time - start_time
                    state_name = SyncDeployedModel.State.Name(deployed_model.state)
                    logger.debug(
                        f"Waiting for deployed model {deployed_model.name} to be ready, "
                        f"current state: {state_name}, elapsed time: {elapsed_so_far:.2f}s"
                    )
                    last_log_time = current_time

                # Wait before next status check
                time.sleep(2)
        elif self.deployment_strategy == "on-demand":

            if deployment is not None and deployment.state == SyncDeployment.State.FAILED:
                logger.debug(f"Deployment {deployment.name} is in FAILED state, deleting it")
                self.delete_deployment()
                logger.debug(f"Successfully deleted failed deployment {deployment.name}")
                deployment = None

            if deployment is None or deployment.state == SyncDeployment.State.DELETED:
                logger.debug(f"No existing deployment found, creating deployment for {self.model}")
                deployment_proto = SyncDeployment(
                    display_name=self.deployment_display_name,
                    base_model=self.model,
                    autoscaling_policy=self._autoscaling_policy_sync,
                )
                if self._accelerator_type_sync is not None:
                    deployment_proto.accelerator_type = self._accelerator_type_sync
                if self._accelerator_count is not None:
                    deployment_proto.accelerator_count = self._accelerator_count
                if self._precision is not None:
                    deployment_proto.precision = getattr(SyncDeployment.Precision, self._precision)
                if self._world_size is not None:
                    deployment_proto.world_size = self._world_size
                if self._generator_count is not None:
                    deployment_proto.generator_count = self._generator_count
                if self._region is not None:
                    deployment_proto.placement.region = getattr(SyncRegion, self._region)
                if self._multi_region is not None:
                    deployment_proto.placement.multi_region = getattr(SyncMultiRegion, self._multi_region)
                if self._description is not None:
                    deployment_proto.description = self._description
                if self._annotations is not None:
                    deployment_proto.annotations.update(self._annotations)
                if self._min_replica_count is not None:
                    deployment_proto.min_replica_count = self._min_replica_count
                else:
                    # default to 0 if not specified
                    deployment_proto.min_replica_count = 0
                if self._max_replica_count is not None:
                    deployment_proto.max_replica_count = self._max_replica_count
                if self._replica_count is not None:
                    deployment_proto.replica_count = self._replica_count
                if self._disaggregated_prefill_count is not None:
                    deployment_proto.disaggregated_prefill_count = self._disaggregated_prefill_count
                if self._disaggregated_prefill_world_size is not None:
                    deployment_proto.disaggregated_prefill_world_size = self._disaggregated_prefill_world_size
                if self._max_batch_size is not None:
                    deployment_proto.max_batch_size = self._max_batch_size
                if self._cluster is not None:
                    deployment_proto.cluster = self._cluster
                if self._enable_addons is not None:
                    deployment_proto.enable_addons = self._enable_addons
                if self._draft_token_count is not None:
                    deployment_proto.draft_token_count = self._draft_token_count
                if self._draft_model is not None:
                    deployment_proto.draft_model = self._draft_model
                if self._ngram_speculation_length is not None:
                    deployment_proto.ngram_speculation_length = self._ngram_speculation_length
                if self._max_peft_batch_size is not None:
                    deployment_proto.max_peft_batch_size = self._max_peft_batch_size
                if self._kv_cache_memory_pct is not None:
                    deployment_proto.kv_cache_memory_pct = self._kv_cache_memory_pct
                if self._enable_session_affinity is not None:
                    deployment_proto.enable_session_affinity = self._enable_session_affinity
                if self._direct_route_api_keys is not None:
                    deployment_proto.direct_route_api_keys.extend(self._direct_route_api_keys)
                if self._num_peft_device_cached is not None:
                    deployment_proto.num_peft_device_cached = self._num_peft_device_cached
                if self._direct_route_type is not None:
                    deployment_proto.direct_route_type = getattr(SyncDirectRouteType, self._direct_route_type)
                if self._direct_route_handle is not None:
                    deployment_proto.direct_route_handle = self._direct_route_handle
                if self._auto_tune_sync.long_prompt:
                    deployment_proto.auto_tune.long_prompt = self._auto_tune_sync.long_prompt
                created_deployment = self._gateway.create_deployment_sync(deployment_proto, self.deployment_id)
                logger.debug(f"Deployment {created_deployment.name} created, waiting for it to be ready")

                if not wait:
                    logger.debug(f"wait=False, not polling for deployment readiness of {created_deployment.name}")
                    return

                # poll deployment status until it's ready
                start_time = time.time()
                last_log_time = 0
                while created_deployment.state != SyncDeployment.State.READY:
                    current_time = time.time()
                    # wait for 9 seconds
                    time.sleep(9)
                    created_deployment = self._gateway.get_deployment_sync(created_deployment.name)
                    if created_deployment is None:
                        raise ValueError(f"Deployment is not found anymore, it was likely deleted while being created")
                    if created_deployment.state == DeploymentState.FAILED:
                        raise ValueError(f"Deployment {created_deployment.name} failed to be created")
                    if created_deployment.state == SyncDeployment.State.DELETED:
                        raise ValueError(f"Deployment {created_deployment.name} was deleted while being created")
                    if created_deployment.state == SyncDeployment.State.DELETING:
                        raise ValueError(f"Deployment {created_deployment.name} is being deleted while being created")
                    if current_time - last_log_time >= 10:
                        elapsed_so_far = current_time - start_time
                        logger.debug(
                            f"Waiting for deployment {created_deployment.name} to be ready, current state: {SyncDeployment.State.Name(created_deployment.state)}, elapsed time: {elapsed_so_far:.2f}s"
                        )
                        last_log_time = current_time

                total_time = time.time() - start_time
                logger.debug(
                    f"Deployment {created_deployment.name} state is READY, checking replicas now (Became READY in {total_time:.2f} seconds)"
                )
            elif isinstance(deployment, SyncDeployment):
                logger.debug(f"Deployment {deployment.name} already exists, checking if it needs to be scaled up")

                field_mask = SyncFieldMask()

                # if autoscaling policy is not equal, update it
                if not self._is_autoscaling_policy_equal(deployment):
                    logger.debug(
                        f"Updating autoscaling policy for {deployment.name} to "
                        f"{self._autoscaling_policy.scale_up_window.total_seconds()}s up, "
                        f"{self._autoscaling_policy.scale_down_window.total_seconds()}s down, "
                        f"{self._autoscaling_policy.scale_to_zero_window.total_seconds()}s to zero"
                    )
                    deployment.autoscaling_policy.scale_up_window = self._autoscaling_policy.scale_up_window  # type: ignore
                    deployment.autoscaling_policy.scale_down_window = self._autoscaling_policy.scale_down_window  # type: ignore
                    deployment.autoscaling_policy.scale_to_zero_window = self._autoscaling_policy.scale_to_zero_window  # type: ignore
                    field_mask.paths.append("autoscaling_policy")

                for field, value in [
                    ("region", self._region),
                    ("description", self._description),
                    ("annotations", self._annotations),
                    ("min_replica_count", self._min_replica_count),
                    ("max_replica_count", self._max_replica_count),
                    ("replica_count", self._replica_count),
                    ("accelerator_count", self._accelerator_count),
                    ("precision", self._precision),
                    ("world_size", self._world_size),
                    ("generator_count", self._generator_count),
                    ("disaggregated_prefill_count", self._disaggregated_prefill_count),
                    ("disaggregated_prefill_world_size", self._disaggregated_prefill_world_size),
                    ("max_batch_size", self._max_batch_size),
                    ("cluster", self._cluster),
                    ("enable_addons", self._enable_addons),
                    ("draft_token_count", self._draft_token_count),
                    ("draft_model", self._draft_model),
                    ("ngram_speculation_length", self._ngram_speculation_length),
                    ("max_peft_batch_size", self._max_peft_batch_size),
                    ("kv_cache_memory_pct", self._kv_cache_memory_pct),
                    ("enable_session_affinity", self._enable_session_affinity),
                    ("direct_route_api_keys", self._direct_route_api_keys),
                    ("num_peft_device_cached", self._num_peft_device_cached),
                    ("direct_route_type", self._direct_route_type),
                    ("direct_route_handle", self._direct_route_handle),
                ]:
                    if value is not None and getattr(deployment, field) != value:
                        logger.debug(f"Updating {field} for {deployment.name} to {value}")
                        setattr(deployment, field, value)
                        field_mask.paths.append(field)

                if (
                    deployment.accelerator_type != self._accelerator_type_sync
                    and self._accelerator_type_sync is not None
                ):
                    raise ValueError(
                        f'Deployment "{deployment.name}" has accelerator type {SyncAcceleratorType.Name(deployment.accelerator_type)}, '
                        f"but LLM has accelerator type {self._accelerator_type}. Please use a different deployment_display_name "
                        f"to use a different accelerator type, as accelerator type cannot be changed for existing deployments."
                    )

                if len(field_mask.paths) > 0:
                    logger.debug(f"Updating deployment {deployment.name} with {field_mask}")
                    start_time = time.time()
                    self._gateway.update_deployment_sync(deployment, field_mask)

                    if not wait:
                        logger.debug(f"wait=False, not polling for deployment update completion of {deployment.name}")
                    else:
                        # poll until deployment is ready
                        while deployment.state != DeploymentState.READY:
                            time.sleep(1)
                            deployment = self._gateway.get_deployment_sync(deployment.name)
                            if deployment is None:
                                raise ValueError(
                                    f"Deployment is not found anymore, it was likely deleted while being updated"
                                )

                        elapsed_time = time.time() - start_time
                        logger.debug(f"Deployment update completed in {elapsed_time:.2f} seconds")

                if deployment.replica_count == 0:
                    logger.debug(f"Deployment {deployment.name} is not ready, scaling to 1 replica")
                    start_time = time.time()
                    self._gateway.scale_deployment_sync(deployment.name, 1)
                    # also send an inference request to wake up the deployment
                    _ = self.chat.completions.acreate(
                        messages=[{"role": "user", "content": 'Say "OK".'}], skip_setup=True
                    )

                    if not wait:
                        logger.debug(
                            f"wait=False, not polling for deployment scale up completion of {deployment.name}"
                        )
                        return

                    # Poll until deployment has at least one replica
                    last_log_time = 0
                    while deployment.replica_count == 0:
                        current_time = time.time()
                        time.sleep(1)
                        deployment = self._gateway.get_deployment_sync(deployment.name)
                        if deployment is None:
                            raise ValueError(
                                f"Deployment is not found anymore, it was likely deleted while being scaled up"
                            )
                        if deployment.state == SyncDeployment.State.FAILED:
                            raise ValueError(f"Deployment {deployment.name} failed to scale up")
                        if deployment.state == SyncDeployment.State.DELETED:
                            raise ValueError(f"Deployment {deployment.name} was deleted while scaling up")
                        if deployment.state == SyncDeployment.State.DELETING:
                            raise ValueError(f"Deployment {deployment.name} is being deleted while scaling up")
                        if current_time - last_log_time >= 10:
                            elapsed_so_far = current_time - start_time
                            logger.debug(
                                f"Waiting for deployment {deployment.name} to scale up, current replicas: {deployment.replica_count}, elapsed time: {elapsed_so_far:.2f}s"
                            )
                            last_log_time = current_time
                            try:
                                self._gateway.scale_deployment_sync(deployment.name, 1)
                            except Exception as e:
                                logger.error(f"Failed to scale deployment {deployment.name}: {e}")

                    total_scale_time = time.time() - start_time
                    logger.debug(f"Deployment {deployment.name} scaled up in {total_scale_time:.2f} seconds")
                logger.debug(f"Deployment {deployment.name} is ready, using deployment")
        else:
            raise ValueError(f"Invalid deployment strategy: {self.deployment_strategy}")

    def scale_to_zero(self) -> Optional[SyncDeployment]:
        """
        Sends a request to scale the deployment to 0 replicas but does not wait for it to complete.
        """
        deployment = self.get_deployment()
        if deployment is None:
            return None
        if isinstance(deployment, SyncDeployedModel):
            raise ValueError(
                f"Deployment {deployment.name} is a LoRA add-on, not a deployment. Please use the deployment_name "
                f"argument to specify a deployment name."
            )
        self._gateway.scale_deployment_sync(deployment.name, 0)
        return deployment

    def scale_to_1_replica(self):
        """
        Scales the deployment to at least 1 replica.
        """
        deployment = self.get_deployment()
        if deployment is None:
            return
        self._gateway.scale_deployment_sync(deployment.name, 1)

    def _is_autoscaling_policy_equal(self, deployment: Union[Deployment, SyncDeployment]) -> bool:
        if isinstance(deployment, SyncDeployment):
            return (
                deployment.autoscaling_policy.scale_up_window == self._autoscaling_policy_sync.scale_up_window
                and deployment.autoscaling_policy.scale_down_window == self._autoscaling_policy_sync.scale_down_window
                and deployment.autoscaling_policy.scale_to_zero_window
                == self._autoscaling_policy_sync.scale_to_zero_window
            )
        return (
            deployment.autoscaling_policy.scale_up_window == self._autoscaling_policy.scale_up_window
            and deployment.autoscaling_policy.scale_down_window == self._autoscaling_policy.scale_down_window
            and deployment.autoscaling_policy.scale_to_zero_window == self._autoscaling_policy.scale_to_zero_window
        )

    @sync_cache
    def get_model(self) -> Optional[SyncModel]:
        return self._gateway.get_model_sync(self.model)

    def is_peft_addon(self) -> bool:
        model = self.get_model()
        if model is None:
            return False
        return model.kind == SyncModel.Kind.HF_PEFT_ADDON

    @property
    def peft_base_model(self) -> Optional[str]:
        """
        If this LLM is a PEFT addon, returns the name of the base model.
        """
        if not self.is_peft_addon():
            return None
        model = self.get_model()
        if model is None:
            return None
        return model.peft_details.base_model

    def list_models(self) -> List[SyncModel]:
        result = []
        page_token = None
        while True:
            response = self._gateway.list_models_sync(
                page_size=200, page_token=page_token if page_token else "", include_deployed_model_refs=True
            )
            result.extend(response.models)

            if not response.next_page_token:
                break
            page_token = response.next_page_token

        return result

    @property
    @sync_cache
    def deployment_url(self) -> Optional[str]:
        """
        Returns the URL to the deployment.
        """
        deployment = self.get_deployment()
        if deployment is None:
            return None
        # get end of "/" split
        id = deployment.name.split("/")[-1]
        if isinstance(deployment, SyncDeployment):
            return f"https://app.fireworks.ai/dashboard/deployments/{id}"
        return f"https://app.fireworks.ai/dashboard/deployedModels/{id}"

    @sync_cache
    def model_id(self):
        """
        Returns the model ID, which is the model name plus the deployment name
        if it exists. This is used for the "model" arg when calling the model.
        """
        if self.is_available_on_serverless() and self.deployment_strategy == "serverless":
            return self.model
        deployment = self.get_deployment()
        if isinstance(deployment, SyncDeployedModel):
            return deployment.name  # accounts/<account_id>/deployedModels/<id>
        if deployment is None:
            if self.deployment_strategy == "on-demand":
                raise ValueError(
                    f"Model {self.model} is not available on serverless and no deployment exists. Make sure to call apply() before calling model_id() or call the model to trigger a deployment."
                )
            else:
                return self.model
        return f"{self.model}#{deployment.name}"

    @property
    def addons_enabled(self) -> bool:
        return False if self._enable_addons is None else self._enable_addons

    @property
    def reinforcement_step(self):
        """Perform a reinforcement learning step."""
        from fireworks.llm.llm_reinforcement_step import LLMReinforcementStep

        return LLMReinforcementStep(self).reinforcement_step

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        attrs = [f"model={self.model}"]
        if self.deployment_url is not None:
            attrs.append(f"deployment_url={self.deployment_url}")
        if self._deployment_display_name is not None:
            attrs.append(f"deployment_display_name={self._deployment_display_name}")
        if self.deployment_type is not None:
            attrs.append(f"deployment_type={self.deployment_type}")
        if self._accelerator_type is not None:
            attrs.append(f"accelerator_type={self._accelerator_type}")
        if self._region is not None:
            attrs.append(f"region={self._region}")
        if self._min_replica_count is not None:
            attrs.append(f"min_replica_count={self._min_replica_count}")
        if self._max_replica_count is not None:
            attrs.append(f"max_replica_count={self._max_replica_count}")
        if self._replica_count is not None:
            attrs.append(f"replica_count={self._replica_count}")
        if self._accelerator_count is not None:
            attrs.append(f"accelerator_count={self._accelerator_count}")
        if self._precision is not None:
            attrs.append(f"precision={self._precision}")
        if self._world_size is not None:
            attrs.append(f"world_size={self._world_size}")
        if self._generator_count is not None:
            attrs.append(f"generator_count={self._generator_count}")
        if self._disaggregated_prefill_count is not None:
            attrs.append(f"disaggregated_prefill_count={self._disaggregated_prefill_count}")
        if self._disaggregated_prefill_world_size is not None:
            attrs.append(f"disaggregated_prefill_world_size={self._disaggregated_prefill_world_size}")
        if self._max_peft_batch_size is not None:
            attrs.append(f"max_peft_batch_size={self._max_peft_batch_size}")
        if self._kv_cache_memory_pct is not None:
            attrs.append(f"kv_cache_memory_pct={self._kv_cache_memory_pct}")
        if self._enable_session_affinity is not None:
            attrs.append(f"enable_session_affinity={self._enable_session_affinity}")
        if self._direct_route_api_keys is not None:
            attrs.append(f"direct_route_api_keys={self._direct_route_api_keys}")
        if self._num_peft_device_cached is not None:
            attrs.append(f"num_peft_device_cached={self._num_peft_device_cached}")
        if self._direct_route_type is not None:
            attrs.append(f"direct_route_type={self._direct_route_type}")
        if self._direct_route_handle is not None:
            attrs.append(f"direct_route_handle={self._direct_route_handle}")
        if self._temperature is not None:
            attrs.append(f"temperature={self._temperature}")
        if self._perf_metrics_in_response is not None:
            attrs.append(f"perf_metrics_in_response={self._perf_metrics_in_response}")
        if self._enable_addons is not None:
            attrs.append(f"enable_addons={self._enable_addons}")
        return f"LLM({', '.join(attrs)})"

    def create_reinforcement_fine_tuning_job(
        self,
        id: str,
        dataset_or_id: Union[Dataset, str],
        reward_function: Callable,
        evaluation_dataset_or_id: Optional[Union[Dataset, str]] = None,
        # BaseTrainingConfig fields
        output_model: Optional[str] = None,
        jinja_template: Optional[str] = None,
        learning_rate: Optional[float] = 0.0001,
        max_context_length: Optional[int] = 8192,
        lora_rank: Optional[int] = 8,
        base_model_weight_precision: Optional[WeightPrecisionLiteral] = None,
        accelerator_type: Optional[AcceleratorTypeLiteral] = None,
        accelerator_count: Optional[int] = None,
        region: Optional[RegionLiteral] = None,
        epochs: Optional[int] = 5,
        batch_size: Optional[int] = 32768,
        is_intermediate: Optional[bool] = None,
        # WandbConfig fields
        wandb_config: Optional[WandbConfigParam] = None,
        # InferenceParameters fields with defaults from command
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = 1.0,
        top_p: Optional[float] = 1.0,
        n: Optional[int] = 8,
        extra_body: Optional[str] = None,
        top_k: Optional[int] = None,
    ):
        if not is_valid_resource_name(id):
            raise ValueError("id must only contain lowercase a-z, 0-9, and hyphen (-)")

        dataset = dataset_or_id if isinstance(dataset_or_id, Dataset) else Dataset.from_id(dataset_or_id)

        evaluation_dataset = (
            evaluation_dataset_or_id
            if isinstance(evaluation_dataset_or_id, Dataset)
            else Dataset.from_id(evaluation_dataset_or_id) if evaluation_dataset_or_id is not None else None
        )
        if evaluation_dataset is not None:
            evaluation_dataset.sync()

        evaluator = Evaluator(
            gateway=self._gateway,
            reward_function=reward_function,
        )
        evaluator.sync()
        training_config = SyncBaseTrainingConfig(
            output_model=(
                output_model
                if output_model is not None
                else generate_model_resource_name(self._gateway.account_id(), id)
            ),
            jinja_template=jinja_template,
            learning_rate=learning_rate,
            max_context_length=max_context_length,
            lora_rank=lora_rank,
            base_model_weight_precision=base_model_weight_precision,
            accelerator_type=accelerator_type,
            accelerator_count=accelerator_count,
            region=region,
            epochs=epochs,
            batch_size=batch_size,
            is_intermediate=is_intermediate if is_intermediate is not None else False,
        )
        if self.is_peft_addon():
            training_config.warm_start_from = self.model
        else:
            training_config.base_model = self.model
        wandb_config = SyncWandbConfig(
            api_key=wandb_config["api_key"],
            project=wandb_config["project"],
            entity=wandb_config["entity"],
        )
        inference_parameters = SyncInferenceParameters(
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            n=n,
            extra_body=extra_body,
            top_k=top_k,
        )
        proto = SyncReinforcementFineTuningJob(
            display_name=id,
            dataset=dataset.name,
            evaluation_dataset=evaluation_dataset.name if evaluation_dataset is not None else None,
            evaluator=evaluator.name,
            training_config=training_config,
            wandb_config=wandb_config,
            inference_parameters=inference_parameters,
        )

        job = ReinforcementFineTuningJob(
            llm=self,
            proto=proto,
            dataset_or_id=dataset_or_id,
            evaluation_dataset_or_id=evaluation_dataset_or_id,
            api_key=self._gateway._api_key,
            id=id,
        )
        job = job.sync()
        logger.debug(f"See the reinforcement fine-tuning job at {job.url}")
        return job

    def create_supervised_fine_tuning_job(
        self,
        display_name: str,
        dataset_or_id: Union[Dataset, str],
        evaluation_dataset_or_id: Optional[Union[Dataset, str]] = None,
        epochs: Optional[int] = None,
        learning_rate: Optional[float] = None,
        lora_rank: Optional[int] = None,
        jinja_template: Optional[str] = None,
        early_stop: Optional[bool] = None,
        max_context_length: Optional[int] = None,
        base_model_weight_precision: Optional[WeightPrecisionLiteral] = None,
        wandb_config: Optional[WandbConfigParam] = None,
        accelerator_type: Optional[AcceleratorTypeLiteral] = None,
        accelerator_count: Optional[int] = None,
        is_turbo: Optional[bool] = None,
        eval_auto_carveout: Optional[bool] = None,
        region: Optional[RegionLiteral] = None,
        nodes: Optional[int] = None,
        batch_size: Optional[int] = None,
        output_model: Optional[str] = None,
    ) -> "SupervisedFineTuningJob":
        """
        Creates a fine-tuning job for this dataset. If the fine-tuning job already exists, it will block until the job is ready.

        Args:
            display_name: The display name of the fine-tuning job. Must only contain lowercase a-z, 0-9, and hyphen (-).
                The display name is also used to identify the fine-tuning job when listing fine-tuning jobs.
            dataset_or_id: The dataset instance to fine-tune on or the dataset id to fine-tune on.
            epochs: The number of epochs to fine-tune for.
            learning_rate: The learning rate to use for fine-tuning.
            lora_rank: The rank to use for LoRA fine-tuning.
            jinja_template: The Jinja template to use for formatting the dataset.
            early_stop: Whether to enable early stopping.
            max_context_length: The maximum context length to use during fine-tuning.
            base_model_weight_precision: The weight precision to use for the base model.
            wandb_config: Configuration for Weights & Biases integration.
            evaluation_dataset: Dataset or dataset id to use for evaluation.
            accelerator_type: The type of accelerator to use for fine-tuning.
            accelerator_count: The number of accelerators to use.
            is_turbo: Whether to use turbo mode for faster fine-tuning.
            eval_auto_carveout: Whether to automatically carve out evaluation data.
            region: The region to run the fine-tuning job in.
            nodes: The number of nodes to use for distributed training.
            batch_size: The batch size to use during training.
            output_model: The name of the output model to create. If not provided, it will be the same as the name argument.

        Returns:
            Fine-tuned LLM
        """
        # Import here to avoid circular import
        from fireworks.supervised_fine_tuning_job import SupervisedFineTuningJob

        if display_name is None:
            raise ValueError("display_name is required")
        if not is_valid_resource_name(display_name):
            raise ValueError("job name must only contain lowercase a-z, 0-9, and hyphen (-)")

        dataset = dataset_or_id if isinstance(dataset_or_id, Dataset) else Dataset.from_id(dataset_or_id)
        evaluation_dataset = (
            evaluation_dataset_or_id
            if isinstance(evaluation_dataset_or_id, Dataset)
            else Dataset.from_id(evaluation_dataset_or_id) if evaluation_dataset_or_id is not None else None
        )

        if wandb_config is not None:
            wandb_config = SyncWandbConfig(
                api_key=wandb_config["api_key"],
                project=wandb_config["project"],
                entity=wandb_config["entity"],
            )
        unique_name = f"{display_name}-{str(uuid4())[:5].lower()}"
        proto = SyncSupervisedFineTuningJob(
            name=f"accounts/{self._gateway.account_id()}/supervisedFineTuningJobs/{unique_name}",
            display_name=display_name,
            epochs=epochs,
            learning_rate=learning_rate,
            lora_rank=lora_rank,
            jinja_template=jinja_template,
            max_context_length=max_context_length,
            base_model_weight_precision=base_model_weight_precision,
            wandb_config=wandb_config,
            dataset=dataset.name,
            evaluation_dataset=evaluation_dataset.name if evaluation_dataset is not None else None,
            accelerator_type=accelerator_type,
            accelerator_count=accelerator_count,
            region=region,
            nodes=nodes,
            batch_size=batch_size,
            output_model=output_model,
        )
        if self.is_peft_addon():
            proto.warm_start_from = self.model
        else:
            proto.base_model = self.model
        if early_stop is not None:
            proto.early_stop = early_stop
        if is_turbo is not None:
            proto.is_turbo = is_turbo
        if eval_auto_carveout is not None:
            proto.eval_auto_carveout = eval_auto_carveout

        job = SupervisedFineTuningJob(
            llm=self,
            proto=proto,
            dataset_or_id=dataset_or_id,
            evaluation_dataset_or_id=evaluation_dataset_or_id,
            api_key=self._gateway._api_key,
        )
        job = job.sync()
        logger.debug(f"See the fine-tuning job at {job.url}")
        return job
