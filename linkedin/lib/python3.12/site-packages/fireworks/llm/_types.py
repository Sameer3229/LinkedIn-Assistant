from typing_extensions import Literal, Required, TypedDict, Union
from openai.types.chat.completion_create_params import ResponseFormat as OpenAIResponseFormat


class ResponseFormatGrammar(TypedDict, total=False):
    type: Required[Literal["grammar"]]
    """The type of response format being defined. Always `text`."""

    grammar: str
    """See https://fireworks.ai/docs/structured-responses/structured-output-grammar-based"""


ResponseFormat = Union[OpenAIResponseFormat, ResponseFormatGrammar]


class WandbConfigParam(TypedDict, total=True):
    """
    Configuration for Weights & Biases (wandb) integration with fine-tuning jobs.

    You must provide ALL three required fields (api_key, project, entity) for wandb logging
    to work properly. Partial configurations will not enable wandb logging.

    Usage Patterns:

    1. **No wandb logging** (default):
       ```python
       wandb_config = None  # No wandb integration
       ```

    2. **Complete configuration** (all three fields required):
       ```python
       wandb_config = {
           "api_key": "your-api-key",
           "project": "your-project",
           "entity": "your-entity"
       }
       ```

    Backend Behavior:
    - Wandb logging is enabled only when ALL three required fields (api_key, project, entity) are present
    - Partial configurations (missing any of the three fields) will NOT enable wandb logging
    - The system automatically generates run IDs and URLs
    - Empty strings are treated as missing fields
    """

    api_key: str
    """
    Weights & Biases API key for authentication.
    
    - If provided: Use this API key for the job
    - If not provided: Wandb logging will be disabled
    
    The API key is automatically encrypted and stored securely.
    """

    project: str
    """
    Weights & Biases project name where metrics will be logged.
    
    - If provided: Use this project for the job
    - If not provided: Wandb logging will be disabled
    
    The project must exist in your wandb account or be created automatically.
    """

    entity: str
    """
    Weights & Biases entity (username or team name).
    
    - If provided: Use this entity for the job
    - If not provided: Wandb logging will be disabled
    
    This can be your personal username or a team/organization name.
    """
