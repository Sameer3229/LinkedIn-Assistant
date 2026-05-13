import time
from datetime import datetime
from typing import Optional, Union, TYPE_CHECKING
from fireworks.gateway import Gateway
from fireworks.dataset import Dataset
from fireworks.control_plane.generated.protos.gateway import (
    JobState,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.batch_inference_job_pb2 import (
    BatchInferenceJob as SyncBatchInferenceJob,
    CreateBatchInferenceJobRequest as SyncCreateBatchInferenceJobRequest,
    ListBatchInferenceJobsRequest as SyncListBatchInferenceJobsRequest,
    InferenceParameters as SyncInferenceParameters,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.status_pb2 import (
    JobState as SyncJobState,
)
from fireworks._logger import logger
from google.protobuf.descriptor import FieldDescriptor


def _enum_to_string(field, value):
    """Convert protobuf enum value to string name.
    
    Args:
        field: The protobuf field descriptor
        value: The enum value (integer)
        
    Returns:
        String representation of the enum value
    """
    if field.type == FieldDescriptor.TYPE_ENUM:
        try:
            # Get the enum descriptor and find the value name
            enum_value = field.enum_type.values_by_number.get(value)
            if enum_value:
                return enum_value.name
        except Exception:
            pass
    return str(value)


class BatchInferenceJob:
    """
    Wrapper around proto for a batch inference job in Fireworks. Provides
    convenient methods for CRUD operations: create, get, list, and delete.
    
    Similar to firectl's batch inference job commands (bij).
    """

    def __init__(self):
        """
        Stateless wrapper for batch inference job operations.
        All operations are performed via class/static methods.
        """
        pass

    @staticmethod
    def _get_job_id_from_name(name: str) -> str:
        """Extract job ID from full resource name."""
        return name.split("/")[-1] if name else ""

    @staticmethod
    def _normalize_job_name(name: str, account: str) -> str:
        """Ensure job name is in full resource format."""
        if not name.startswith("accounts/"):
            return f"accounts/{account}/batchInferenceJobs/{name}"
        return name

    @staticmethod
    def get(job_id: str, account: str, api_key: Optional[str] = None) -> Optional[SyncBatchInferenceJob]:
        """
        Get a batch inference job by its ID.
        Equivalent to: firectl get bij <job-id>
        
        Args:
            job_id: The job ID (e.g., "test-job-123") or full resource name
            account: Account ID
            api_key: The API key to use
            
        Returns:
            BatchInferenceJob proto if found, None otherwise
        """
        gateway = Gateway(api_key=api_key)
        
        name = BatchInferenceJob._normalize_job_name(job_id, account)
        
        proto = gateway.get_batch_inference_job_sync(name)
        if proto is None:
            return None
            
        return proto

    @staticmethod
    def list(
        account: str,
        api_key: Optional[str] = None,
        page_size: int = 50
    ) -> list[SyncBatchInferenceJob]:
        """
        List batch inference jobs in an account.
        Equivalent to: firectl list bij
        
        Args:
            account: Account ID
            api_key: The API key to use
            page_size: Number of jobs to return per page
            
        Returns:
            List of BatchInferenceJob protos
        """
        gateway = Gateway(api_key=api_key)
        
        request = SyncListBatchInferenceJobsRequest()
        request.parent = f"accounts/{account}"
        request.page_size = page_size
        
        response = gateway._sync_stub.ListBatchInferenceJobs(request)
        
        return list(response.batch_inference_jobs)

    @staticmethod
    def create(
        model: str,
        input_dataset_id: str,
        output_dataset_id: Optional[str] = None,
        job_id: Optional[str] = None,
        display_name: Optional[str] = None,
        inference_parameters: Optional[dict] = None,
        api_key: Optional[str] = None,
    ) -> SyncBatchInferenceJob:
        """
        Create a new batch inference job.
        Equivalent to: firectl create bij --model <model> --input-dataset-id <dataset>
        
        Args:
            model: The model to use for inference
            input_dataset_id: The input dataset ID
            output_dataset_id: The output dataset ID (optional)
            job_id: The job ID (optional, will be auto-generated if not provided)
            display_name: Display name for the job (optional)
            inference_parameters: Dict of inference parameters like max_tokens, temperature, etc.
            api_key: The API key to use
            
        Returns:
            BatchInferenceJob proto
        """
        gateway = Gateway(api_key=api_key)
        account_id = gateway.account_id()
        
        # Normalize resource names
        if not model.startswith("accounts/"):
            model = f"accounts/{account_id}/models/{model}"
        if not input_dataset_id.startswith("accounts/"):
            input_dataset_id = f"accounts/{account_id}/datasets/{input_dataset_id}"
        if output_dataset_id and not output_dataset_id.startswith("accounts/"):
            output_dataset_id = f"accounts/{account_id}/datasets/{output_dataset_id}"
        
        # Create the batch inference job proto
        job_proto = SyncBatchInferenceJob()
        job_proto.model = model
        job_proto.input_dataset_id = input_dataset_id
        if output_dataset_id:
            job_proto.output_dataset_id = output_dataset_id
        if display_name:
            job_proto.display_name = display_name
            
        # Set inference parameters if provided
        if inference_parameters:
            params = SyncInferenceParameters()
            
            if "max_tokens" in inference_parameters:
                params.max_tokens = inference_parameters["max_tokens"]
            if "temperature" in inference_parameters:
                params.temperature = inference_parameters["temperature"]
            if "top_p" in inference_parameters:
                params.top_p = inference_parameters["top_p"]
            if "top_k" in inference_parameters:
                params.top_k = inference_parameters["top_k"]
            if "n" in inference_parameters:
                params.n = inference_parameters["n"]
            if "extra_body" in inference_parameters:
                params.extra_body = inference_parameters["extra_body"]
                
            job_proto.inference_parameters.CopyFrom(params)
        
        # Create the request
        request = SyncCreateBatchInferenceJobRequest()
        request.batch_inference_job.CopyFrom(job_proto)
        if job_id:
            request.batch_inference_job_id = job_id
        
        # Create the job
        created_proto = gateway.create_batch_inference_job_sync(request)
        return created_proto


    @staticmethod
    def delete(job_id: str, account: str, api_key: Optional[str] = None) -> None:
        """
        Delete a batch inference job by ID.
        Equivalent to: firectl delete bij <job-id>
        
        Args:
            job_id: The job ID or full resource name
            account: Account ID
            api_key: The API key to use
        """
        gateway = Gateway(api_key=api_key)
        
        name = BatchInferenceJob._normalize_job_name(job_id, account)
        
        gateway.delete_batch_inference_job_sync(name)

    @staticmethod
    def to_dict(proto: SyncBatchInferenceJob) -> dict:
        """Convenience method to convert a batch inference job proto to a friendly representation."""
        if not proto:
            return {}
        
        result = {}
        for field, value in proto.ListFields():
            if field.name in ['name', 'display_name', 'model', 'input_dataset_id', 'output_dataset_id', 'created_by']:
                result[field.name] = str(value)
            elif field.type == FieldDescriptor.TYPE_ENUM:
                # Convert any enum field to readable string name
                result[field.name] = _enum_to_string(field, value)
            elif field.name in ['create_time', 'update_time']:
                # Convert timestamp to readable format in UTC
                if hasattr(value, 'seconds') and hasattr(value, 'nanos'):
                    timestamp = value.seconds + value.nanos / 1e9
                    dt = datetime.utcfromtimestamp(timestamp)
                    result[field.name] = dt.strftime('%Y-%m-%d %H:%M:%S UTC')
                else:
                    result[field.name] = str(value)
            elif field.name == 'inference_parameters':
                params = {}
                for param_field, param_value in value.ListFields():
                    params[param_field.name] = param_value
                result['inference_parameters'] = params
            elif field.name == 'status' and hasattr(value, 'message'):
                result['status_message'] = value.message
        
        return result
