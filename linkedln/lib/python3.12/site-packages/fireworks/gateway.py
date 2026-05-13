# Copyright (c) Fireworks AI, Inc. and affiliates.
#
# All Rights Reserved.

import os
import time
from typing import List, Optional, TypeVar, Union

from fireworks._const import FIREWORKS_API_BASE_URL, FIREWORKS_GATEWAY_ADDR
from fireworks._util import get_api_key_from_env
import grpclib
import grpc
from grpc._channel import _InactiveRpcError
from grpclib.client import Channel
import httpx
from functools import cache as sync_cache
from betterproto.lib.std.google.protobuf import FieldMask
from google.protobuf.field_mask_pb2 import FieldMask as SyncFieldMask
from fireworks.control_plane.generated.protos_grpcio.gateway.rlor_trainer_job_pb2 import (
    CreateRlorTrainerJobRequest as SyncCreateRlorTrainerJobRequest,
    RlorTrainerJob as SyncRlorTrainerJob,
    GetRlorTrainerJobRequest as SyncGetRlorTrainerJobRequest,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.gateway_pb2_grpc import GatewayStub as SyncGatewayStub
from fireworks.control_plane.generated.protos_grpcio.gateway.supervised_fine_tuning_job_pb2 import (
    SupervisedFineTuningJob as SyncSupervisedFineTuningJob,
    CreateSupervisedFineTuningJobRequest as SyncCreateSupervisedFineTuningJobRequest,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.reinforcement_fine_tuning_job_pb2 import (
    ReinforcementFineTuningJob as SyncReinforcementFineTuningJob,
    CreateReinforcementFineTuningJobRequest as SyncCreateReinforcementFineTuningJobRequest,
    GetReinforcementFineTuningJobRequest as SyncGetReinforcementFineTuningJobRequest,
    ListReinforcementFineTuningJobsRequest as SyncListReinforcementFineTuningJobsRequest,
    ListReinforcementFineTuningJobsResponse as SyncListReinforcementFineTuningJobsResponse,
    DeleteReinforcementFineTuningJobRequest as SyncDeleteReinforcementFineTuningJobRequest,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.deployed_model_pb2 import (
    DeployedModel as SyncDeployedModel,
    CreateDeployedModelRequest as SyncCreateDeployedModelRequest,
    GetDeployedModelRequest as SyncGetDeployedModelRequest,
    ListDeployedModelsRequest as SyncListDeployedModelsRequest,
    ListDeployedModelsResponse as SyncListDeployedModelsResponse,
    DeleteDeployedModelRequest as SyncDeleteDeployedModelRequest,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.dataset_pb2 import (
    Dataset as SyncDataset,
    CreateDatasetRequest as SyncCreateDatasetRequest,
    DeleteDatasetRequest as SyncDeleteDatasetRequest,
    ListDatasetsRequest as SyncListDatasetsRequest,
    ListDatasetsResponse as SyncListDatasetsResponse,
    GetDatasetUploadEndpointRequest as SyncGetDatasetUploadEndpointRequest,
    GetDatasetRequest as SyncGetDatasetRequest,
    ValidateDatasetUploadRequest as SyncValidateDatasetUploadRequest,
    GetDatasetDownloadEndpointRequest as SyncGetDatasetDownloadEndpointRequest,
    GetDatasetDownloadEndpointResponse as SyncGetDatasetDownloadEndpointResponse,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.supervised_fine_tuning_job_pb2 import (
    ListSupervisedFineTuningJobsRequest as SyncListSupervisedFineTuningJobsRequest,
    ListSupervisedFineTuningJobsResponse as SyncListSupervisedFineTuningJobsResponse,
    DeleteSupervisedFineTuningJobRequest as SyncDeleteSupervisedFineTuningJobRequest,
    GetSupervisedFineTuningJobRequest as SyncGetSupervisedFineTuningJobRequest,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.batch_inference_job_pb2 import (
    BatchInferenceJob as SyncBatchInferenceJob,
    CreateBatchInferenceJobRequest as SyncCreateBatchInferenceJobRequest,
    GetBatchInferenceJobRequest as SyncGetBatchInferenceJobRequest,
    ListBatchInferenceJobsRequest as SyncListBatchInferenceJobsRequest,
    ListBatchInferenceJobsResponse as SyncListBatchInferenceJobsResponse,
    DeleteBatchInferenceJobRequest as SyncDeleteBatchInferenceJobRequest,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.deployment_pb2 import (
    ListDeploymentsRequest as SyncListDeploymentsRequest,
    UpdateDeploymentRequest as SyncUpdateDeploymentRequest,
    Deployment as SyncDeployment,
    AutoscalingPolicy as SyncAutoscalingPolicy,
    AcceleratorType as SyncAcceleratorType,
    CreateDeploymentRequest as SyncCreateDeploymentRequest,
    ScaleDeploymentRequest as SyncScaleDeploymentRequest,
    GetDeploymentRequest as SyncGetDeploymentRequest,
    DeleteDeploymentRequest as SyncDeleteDeploymentRequest,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.model_pb2 import (
    ListServerlessLoraModelsRequest as SyncListServerlessLoraModelsRequest,
    ListServerlessLoraModelsResponse as SyncListServerlessLoraModelsResponse,
    Model as SyncModel,
    GetModelRequest as SyncGetModelRequest,
    ListModelsRequest as SyncListModelsRequest,
    ListModelsResponse as SyncListModelsResponse,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.evaluator_pb2 import (
    PreviewEvaluatorRequest as SyncPreviewEvaluatorRequest,
    PreviewEvaluatorResponse as SyncPreviewEvaluatorResponse,
    GetEvaluatorRequest as SyncGetEvaluatorRequest,
    Evaluator as SyncEvaluator,
    CreateEvaluatorRequest as SyncCreateEvaluatorRequest,
    ListEvaluatorsRequest as SyncListEvaluatorsRequest,
    ListEvaluatorsResponse as SyncListEvaluatorsResponse,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.evaluation_job_pb2 import (
    CreateEvaluationJobRequest as SyncCreateEvaluationJobRequest,
    EvaluationJob as SyncEvaluationJob,
    GetEvaluationJobRequest as SyncGetEvaluationJobRequest,
)
from fireworks.control_plane.generated.protos.gateway import (
    AcceleratorType,
    AutoscalingPolicy,
    CreateDatasetRequest,
    CreateDeploymentRequest,
    CreateSupervisedFineTuningJobRequest,
    Dataset,
    DeleteDatasetRequest,
    DeleteSupervisedFineTuningJobRequest,
    Deployment,
    GatewayStub,
    GetDatasetUploadEndpointRequest,
    GetDeploymentRequest,
    GetSupervisedFineTuningJobRequest,
    ListDatasetsRequest,
    ListDeploymentsRequest,
    ListModelsRequest,
    ListModelsResponse,
    ListSupervisedFineTuningJobsRequest,
    ListSupervisedFineTuningJobsResponse,
    Model,
    ScaleDeploymentRequest,
    SupervisedFineTuningJob,
    UpdateDeploymentRequest,
    CreateDatasetValidationJobRequest,
    ValidateDatasetUploadRequest,
)
from asyncstdlib.functools import cache
from openai import NOT_GIVEN, NotGiven

from grpc import (
    AuthMetadataPlugin,
)


class CustomAuthMetadata(AuthMetadataPlugin):
    def __init__(self, api_key: str):
        self._api_key = api_key

    def __call__(self, context, callback):
        from fireworks import __version__

        metadata = [("x-api-key", self._api_key), ("x-python-sdk-version", __version__)]
        callback(metadata, None)


class CustomAuthInterceptor(
    grpc.UnaryUnaryClientInterceptor,
    grpc.UnaryStreamClientInterceptor,
    grpc.StreamUnaryClientInterceptor,
    grpc.StreamStreamClientInterceptor,
):
    def __init__(self, api_key: str):
        self._api_key = api_key

    def intercept_unary_unary(self, continuation, client_call_details, request):
        from fireworks import __version__

        metadata = list(client_call_details.metadata or [])
        metadata.append(("x-api-key", self._api_key))
        new_details = client_call_details._replace(metadata=metadata)
        return continuation(new_details, request)

    def intercept_unary_stream(self, continuation, client_call_details, request):
        from fireworks import __version__

        metadata = list(client_call_details.metadata or [])
        metadata.append(("x-api-key", self._api_key))
        new_details = client_call_details._replace(metadata=metadata)
        return continuation(new_details, request)

    def intercept_stream_unary(self, continuation, client_call_details, request_iterator):
        from fireworks import __version__

        metadata = list(client_call_details.metadata or [])
        metadata.append(("x-api-key", self._api_key))
        new_details = client_call_details._replace(metadata=metadata)
        return continuation(new_details, request_iterator)

    def intercept_stream_stream(self, continuation, client_call_details, request_iterator):
        from fireworks import __version__

        metadata = list(client_call_details.metadata or [])
        metadata.append(("x-api-key", self._api_key))
        new_details = client_call_details._replace(metadata=metadata)
        return continuation(new_details, request_iterator)


R = TypeVar("R")


class Gateway:
    """
    Control plane gateway client that exposes its endpoints through
    convenient APIs.

    Keep the API consistent with `gateway.proto`.
    """

    def __init__(
        self,
        *,
        server_addr: str = FIREWORKS_GATEWAY_ADDR,
        api_key: Optional[str] = None,
    ) -> None:
        """
        Args:
            server_addr: the network address of the gateway server.
            api_key: the API key to use for authentication.
        """
        self._server_addr = server_addr
        if not api_key:
            api_key = get_api_key_from_env()
            if not api_key:
                raise ValueError(
                    "Fireworks API key not found. Please provide an API key either as a parameter "
                    "or by setting the FIREWORKS_API_KEY environment variable. "
                    "You can create a new API key at https://fireworks.ai/settings/users/api-keys or "
                    "by using `firectl create api-key --key-name <key-name>` command."
                )
        self._api_key = api_key
        self._host = self._server_addr.split(":")[0]
        self._port = int(self._server_addr.split(":")[1])

        from fireworks import __version__

        user_agent_option = ("grpc.primary_user_agent", f"fireworks-python-sdk/{__version__}")
        # Only use SSL credentials if port is 443, but always include API key auth
        if self._port == 443:
            creds = grpc.composite_channel_credentials(
                grpc.ssl_channel_credentials(),
                grpc.metadata_call_credentials(CustomAuthMetadata(api_key)),
            )
            self._sync_channel = grpc.secure_channel(self._server_addr, creds, options=[user_agent_option])
        else:
            # For non-SSL connections, still need to add API key auth
            self._sync_channel = grpc.insecure_channel(self._server_addr, [user_agent_option])
            self._sync_channel = grpc.intercept_channel(self._sync_channel, CustomAuthInterceptor(api_key))

        self._sync_stub = SyncGatewayStub(self._sync_channel)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self._sync_channel.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self._sync_channel.close()

    def create_reinforcement_fine_tuning_job_sync(
        self, request: SyncCreateReinforcementFineTuningJobRequest
    ) -> SyncReinforcementFineTuningJob:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        response = self._sync_stub.CreateReinforcementFineTuningJob(request)
        return response

    def get_reinforcement_fine_tuning_job_sync(self, id: str) -> Optional[SyncReinforcementFineTuningJob]:
        try:
            account_id = self.account_id()
            response = self._sync_stub.GetReinforcementFineTuningJob(
                SyncGetReinforcementFineTuningJobRequest(
                    name=f"accounts/{account_id}/reinforcementFineTuningJobs/{id}"
                )
            )
            return response
        except _InactiveRpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                return None
            raise e

    def list_reinforcement_fine_tuning_jobs_sync(
        self, request: SyncListReinforcementFineTuningJobsRequest
    ) -> SyncListReinforcementFineTuningJobsResponse:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        response = self._sync_stub.ListReinforcementFineTuningJobs(request)
        return response

    def delete_reinforcement_fine_tuning_job_sync(self, id: str) -> None:
        account_id = self.account_id()
        self._sync_stub.DeleteReinforcementFineTuningJob(
            SyncDeleteReinforcementFineTuningJobRequest(name=f"accounts/{account_id}/reinforcementFineTuningJobs/{id}")
        )

    async def create_supervised_fine_tuning_job(
        self, request: CreateSupervisedFineTuningJobRequest
    ) -> SupervisedFineTuningJob:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        response = await self._stub.create_supervised_fine_tuning_job(request)
        return response

    def create_supervised_fine_tuning_job_sync(
        self, request: SyncCreateSupervisedFineTuningJobRequest
    ) -> SupervisedFineTuningJob:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        response = self._sync_stub.CreateSupervisedFineTuningJob(request)
        return response

    async def delete_supervised_fine_tuning_job(self, name: str) -> None:
        try:
            await self._stub.delete_supervised_fine_tuning_job(DeleteSupervisedFineTuningJobRequest(name=name))
        except grpclib.exceptions.GRPCError as e:
            if e.status == grpclib.Status.NOT_FOUND:
                return
            raise e

    def delete_supervised_fine_tuning_job_sync(self, name: str) -> None:
        try:
            self._sync_stub.DeleteSupervisedFineTuningJob(SyncDeleteSupervisedFineTuningJobRequest(name=name))
        except _InactiveRpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                return
            raise e

    async def list_supervised_fine_tuning_jobs(
        self, request: ListSupervisedFineTuningJobsRequest
    ) -> ListSupervisedFineTuningJobsResponse:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        request.page_size = 200
        response = await self._stub.list_supervised_fine_tuning_jobs(request)
        return response

    def list_supervised_fine_tuning_jobs_sync(
        self, request: SyncListSupervisedFineTuningJobsRequest
    ) -> SyncListSupervisedFineTuningJobsResponse:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        request.page_size = 200

        max_retries = 3
        base_delay = 1.0  # Start with 1 second delay

        for attempt in range(max_retries):
            try:
                response = self._sync_stub.ListSupervisedFineTuningJobs(request)
                return response
            except _InactiveRpcError as e:
                if e.code() != grpc.StatusCode.UNAVAILABLE:
                    raise e
                if attempt == max_retries - 1:  # Last attempt
                    raise e
                delay = base_delay * (2**attempt)  # Exponential backoff
                time.sleep(delay)
                continue
        raise Exception("Failed to list supervised fine tuning jobs")

    async def get_supervised_fine_tuning_job(self, name: str) -> Optional[SupervisedFineTuningJob]:
        try:
            response = await self._stub.get_supervised_fine_tuning_job(GetSupervisedFineTuningJobRequest(name=name))
            return response
        except grpclib.exceptions.GRPCError as e:
            if e.status == grpclib.Status.NOT_FOUND:
                return None
            raise e

    def get_supervised_fine_tuning_job_sync(self, name: str) -> Optional[SyncSupervisedFineTuningJob]:
        try:
            response = self._sync_stub.GetSupervisedFineTuningJob(SyncGetSupervisedFineTuningJobRequest(name=name))
            return response
        except _InactiveRpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                return None
            raise e

    def create_batch_inference_job_sync(self, request: SyncCreateBatchInferenceJobRequest) -> SyncBatchInferenceJob:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        response = self._sync_stub.CreateBatchInferenceJob(request)
        return response

    def get_batch_inference_job_sync(self, name: str) -> Optional[SyncBatchInferenceJob]:
        try:
            response = self._sync_stub.GetBatchInferenceJob(SyncGetBatchInferenceJobRequest(name=name))
            return response
        except _InactiveRpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                return None
            raise e

    def list_batch_inference_jobs_sync(
        self, request: SyncListBatchInferenceJobsRequest
    ) -> SyncListBatchInferenceJobsResponse:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        request.page_size = 200

        max_retries = 3
        base_delay = 1.0  # Start with 1 second delay

        for attempt in range(max_retries):
            try:
                response = self._sync_stub.ListBatchInferenceJobs(request)
                return response
            except _InactiveRpcError as e:
                if attempt == max_retries - 1:  # Last attempt
                    raise e
                if e.code() == grpc.StatusCode.UNAVAILABLE:
                    delay = base_delay * (2**attempt)  # Exponential backoff
                    time.sleep(delay)
                else:
                    raise e
        raise Exception("Failed to list batch inference jobs")

    def delete_batch_inference_job_sync(self, name: str) -> None:
        try:
            self._sync_stub.DeleteBatchInferenceJob(SyncDeleteBatchInferenceJobRequest(name=name))
        except _InactiveRpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                return
            raise e

    async def list_datasets(
        self,
        request: ListDatasetsRequest,
    ) -> List[Dataset]:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        response = await self._stub.list_datasets(request)
        return response.datasets

    async def get_dataset_sync(self, name: str) -> SyncDataset:
        account_id = self.account_id()
        response = await self._sync_stub.GetDataset(
            SyncGetDatasetRequest(name=f"accounts/{account_id}/datasets/{name}")
        )
        return response

    def list_datasets_sync(
        self,
        request: SyncListDatasetsRequest,
    ) -> SyncListDatasetsResponse:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        response: SyncListDatasetsResponse = self._sync_stub.ListDatasets(request)
        return response

    async def delete_dataset(self, name: str) -> None:
        account_id = self.account_id()
        await self._stub.delete_dataset(DeleteDatasetRequest(name=f"accounts/{account_id}/datasets/{name}"))

    def delete_dataset_sync(self, name: str) -> None:
        account_id = self.account_id()
        self._sync_stub.DeleteDataset(SyncDeleteDatasetRequest(name=f"accounts/{account_id}/datasets/{name}"))

    async def validate_dataset(self, name: str) -> None:
        account_id = self.account_id()
        await self._stub.validate_dataset_upload(
            ValidateDatasetUploadRequest(name=f"accounts/{account_id}/datasets/{name}")
        )

    def validate_dataset_sync(self, name: str) -> None:
        account_id = self.account_id()
        self._sync_stub.ValidateDatasetUpload(
            SyncValidateDatasetUploadRequest(name=f"accounts/{account_id}/datasets/{name}")
        )

    async def create_dataset(
        self,
        request: CreateDatasetRequest,
    ) -> Dataset:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        response = await self._stub.create_dataset(request)
        return response

    def create_dataset_sync(
        self,
        request: SyncCreateDatasetRequest,
    ) -> SyncDataset:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        response = self._sync_stub.CreateDataset(request)
        return response

    def get_dataset_download_endpoint_sync(self, id: str) -> Optional[SyncGetDatasetDownloadEndpointResponse]:
        try:
            account_id = self.account_id()
            response = self._sync_stub.GetDatasetDownloadEndpoint(
                SyncGetDatasetDownloadEndpointRequest(name=f"accounts/{account_id}/datasets/{id}")
            )
            return response
        except _InactiveRpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                return None
            raise e

    async def get_dataset_upload_endpoint(
        self,
        name: str,
        filename_to_size: dict[str, int],
    ) -> dict[str, str]:
        account_id = self.account_id()
        name = f"accounts/{account_id}/datasets/{name}"
        response = await self._stub.get_dataset_upload_endpoint(
            GetDatasetUploadEndpointRequest(name=name, filename_to_size=filename_to_size)
        )
        return response.filename_to_signed_urls

    def get_dataset_upload_endpoint_sync(
        self,
        name: str,
        filename_to_size: dict[str, int],
    ) -> dict[str, str]:
        account_id = self.account_id()
        name = f"accounts/{account_id}/datasets/{name}"
        response = self._sync_stub.GetDatasetUploadEndpoint(
            SyncGetDatasetUploadEndpointRequest(name=name, filename_to_size=filename_to_size)
        )
        return response.filename_to_signed_urls

    async def list_models(
        self,
        *,
        parent: str = "",
        filter: str = "",
        order_by: str = "",
        include_deployed_model_refs: bool = False,
    ) -> List[Model]:
        """
        Paginates through the list of available models and returns all of them.

        Args:
            parent: resource name of the parent account,
            filter: only models satisfying the provided filter (if specified)
                will be returned. See https://google.aip.dev/160 for the filter
                grammar,
            order_by: a comma-separated list of fields to order by. e.g. "foo,bar".
                The default sort order is ascending. To specify a descending order
                for a field, append a " desc" suffix. e.g. "foo desc,bar"
                Subfields are specified with a "." character. e.g. "foo.bar".
                If not specified, the default order is by "name".

        Returns:
            list of models satisfying the retrieval criteria.
        """
        result = []
        page_token = None
        while True:
            request = ListModelsRequest(
                parent=parent,
                filter=filter,
                order_by=order_by,
                include_deployed_model_refs=include_deployed_model_refs,
                page_size=200,
            )
            if page_token is not None:
                request.page_token = page_token
            response: ListModelsResponse = await self._stub.list_models(request)
            result.extend(response.models)
            if response.total_size < len(result):
                return result
            elif response.total_size == len(result):
                return result
            page_token = response.next_page_token

    def list_models_sync(
        self,
        *,
        page_size: int = 200,
        page_token: str = "",
        filter: str = "",
        order_by: str = "",
        include_deployed_model_refs: bool = False,
        parent: Optional[str] = None,
    ) -> SyncListModelsResponse:
        if parent is None:
            parent = f"accounts/{self.account_id()}"
        request = SyncListModelsRequest(
            parent=parent,
            page_size=page_size,
            page_token=page_token,
            filter=filter,
            order_by=order_by,
            include_deployed_model_refs=include_deployed_model_refs,
        )
        response = self._sync_stub.ListModels(request)
        return response

    async def list_deployments(self, filter: str = ""):
        account_id = self.account_id()
        deployments = await self._stub.list_deployments(
            ListDeploymentsRequest(parent=f"accounts/{account_id}", filter=filter)
        )
        return deployments.deployments

    def list_deployments_sync(self, filter: str = "") -> List[SyncDeployment]:
        account_id = self.account_id()
        deployments = self._sync_stub.ListDeployments(
            SyncListDeploymentsRequest(parent=f"accounts/{account_id}", filter=filter)
        )
        return deployments.deployments

    def list_serverless_lora_sync(self) -> SyncListServerlessLoraModelsResponse:
        loras = self._sync_stub.ListServerlessLoraModels(SyncListServerlessLoraModelsRequest())
        return loras

    def create_deployed_model_sync(self, request: SyncCreateDeployedModelRequest) -> SyncDeployedModel:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        return self._sync_stub.CreateDeployedModel(request)

    def get_deployed_model_sync(self, name: str) -> Optional[SyncDeployedModel]:
        try:
            return self._sync_stub.GetDeployedModel(SyncGetDeployedModelRequest(name=name))
        except _InactiveRpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                return None
            raise e

    def list_deployed_models_sync(self, request: SyncListDeployedModelsRequest) -> SyncListDeployedModelsResponse:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        return self._sync_stub.ListDeployedModels(request)

    def delete_deployed_model_sync(self, name: str) -> None:
        try:
            self._sync_stub.DeleteDeployedModel(SyncDeleteDeployedModelRequest(name=name))
        except _InactiveRpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                return
            raise e

    async def create_deployment(
        self,
        deployment: Deployment,
    ):
        account_id = self.account_id()
        request = CreateDeploymentRequest(parent=f"accounts/{account_id}", deployment=deployment)
        created_deployment = await self._stub.create_deployment(request)
        return created_deployment

    def create_deployment_sync(
        self,
        deployment: SyncDeployment,
        deployment_id: Optional[str] = None,
    ):
        account_id = self.account_id()
        request = SyncCreateDeploymentRequest(
            parent=f"accounts/{account_id}", deployment=deployment, deployment_id=deployment_id
        )
        created_deployment = self._sync_stub.CreateDeployment(request, metadata=[("x-api-key", self._api_key)])
        return created_deployment

    def create_rlor_trainer_job_sync(
        self,
        request: SyncCreateRlorTrainerJobRequest,
    ) -> SyncRlorTrainerJob:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        return self._sync_stub.CreateRlorTrainerJob(request)

    def get_rlor_trainer_job_sync(self, name: str) -> Optional[SyncRlorTrainerJob]:
        try:
            return self._sync_stub.GetRlorTrainerJob(SyncGetRlorTrainerJobRequest(name=name))
        except _InactiveRpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                return None
            raise e

    async def scale_deployment(self, name: str, replicas: int):
        await self._stub.scale_deployment(ScaleDeploymentRequest(name=name, replica_count=replicas))

    def scale_deployment_sync(self, name: str, replicas: int):
        self._sync_stub.ScaleDeployment(SyncScaleDeploymentRequest(name=name, replica_count=replicas))

    def delete_deployment_sync(self, name: str, ignore_checks: bool = False, hard: bool = False):
        if not name.startswith("accounts/"):
            name = f"accounts/{self.account_id()}/deployments/{name}"
        self._sync_stub.DeleteDeployment(
            SyncDeleteDeploymentRequest(name=name, ignore_checks=ignore_checks, hard=hard)
        )

    def preview_evaluator_sync(self, request: SyncPreviewEvaluatorRequest) -> SyncPreviewEvaluatorResponse:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        return self._sync_stub.PreviewEvaluator(request)

    def get_evaluator_sync(self, name: str) -> Optional[SyncEvaluator]:
        try:
            if not name.startswith("accounts/"):
                name = f"accounts/{self.account_id()}/evaluators/{name}"
            return self._sync_stub.GetEvaluator(SyncGetEvaluatorRequest(name=name))
        except _InactiveRpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                return None
            raise e

    def list_evaluators_sync(self, request: SyncListEvaluatorsRequest) -> SyncListEvaluatorsResponse:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        return self._sync_stub.ListEvaluators(request)

    def create_evaluator_sync(self, request: SyncCreateEvaluatorRequest) -> SyncEvaluator:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        return self._sync_stub.CreateEvaluator(request)

    def create_evaluation_job_sync(self, request: SyncCreateEvaluationJobRequest) -> SyncEvaluationJob:
        account_id = self.account_id()
        request.parent = f"accounts/{account_id}"
        return self._sync_stub.CreateEvaluationJob(request)

    def get_evaluation_job_sync(self, name: str) -> Optional[SyncEvaluationJob]:
        if not name:
            return None
        if not name.startswith("accounts/"):
            name = f"accounts/{self.account_id()}/evaluation_jobs/{name}"
        return self._sync_stub.GetEvaluationJob(SyncGetEvaluationJobRequest(name=name))

    async def update_deployment(
        self,
        name: str,
        autoscaling_policy: Optional[AutoscalingPolicy] = None,
        accelerator_type: Optional[AcceleratorType] = None,
    ):
        deployment = Deployment(name=name)
        update_mask = FieldMask(paths=[])
        if autoscaling_policy is not None:
            deployment.autoscaling_policy = autoscaling_policy
            update_mask.paths.append("autoscaling_policy")
        if accelerator_type is not None:
            deployment.accelerator_type = accelerator_type
            update_mask.paths.append("accelerator_type")
        if len(update_mask.paths) == 0:
            return
        await self._stub.update_deployment(UpdateDeploymentRequest(deployment=deployment, update_mask=update_mask))

    def update_deployment_sync(
        self,
        deployment: SyncDeployment,
        update_mask: SyncFieldMask,
    ):
        self._sync_stub.UpdateDeployment(SyncUpdateDeploymentRequest(deployment=deployment, update_mask=update_mask))

    async def get_deployment(self, name: str) -> Deployment:
        return await self._stub.get_deployment(GetDeploymentRequest(name=name))

    def get_deployment_sync(self, name: str) -> Optional[SyncDeployment]:
        try:
            return self._sync_stub.GetDeployment(SyncGetDeploymentRequest(name=name))
        except _InactiveRpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                return None
            raise e

    def get_model_sync(self, name: str) -> Optional[SyncModel]:
        try:
            return self._sync_stub.GetModel(SyncGetModelRequest(name=name))
        except _InactiveRpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                return None
            raise e

    @sync_cache
    def account_id(self) -> str:
        # make curl -v -H "Authorization: Bearer XXX" https://api.fireworks.ai/verifyApiKey
        # and read x-fireworks-account-id from headers of the response
        with httpx.Client() as client:
            response = client.get(
                f"{FIREWORKS_API_BASE_URL}/verifyApiKey",
                headers={
                    "Authorization": f"Bearer {self._api_key}",
                },
            )
            return response.headers["x-fireworks-account-id"]
