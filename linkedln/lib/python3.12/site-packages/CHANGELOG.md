# python

## 0.19.20

### Patch Changes

- a09f41f: Fix supervised fine tuning for peft addons

## 0.19.19

### Patch Changes

- f7ac146: stub reward-kit and make it optional

## 0.19.18

### Patch Changes

- ba39f17: add accelerator type/accelerator count to reinforcement_step()

## 0.19.17

### Patch Changes

- 4f4ea6a: Fix protobuf import conflict with googleapis-common-protos.

  Resolves TypeError when both googleapis-common-protos and fireworks-ai are installed by removing duplicate Google API protobuf files and adding googleapis-common-protos as a dependency.

## 0.19.16

### Patch Changes

- 8902d14: fix wandb_config parameter and make evaluation_dataset kwarg consistent with dataset
- 07694dc: remove extraneous gRPC channel and add "atexit" callbacks

## 0.19.15

### Patch Changes

- b08020e: Allow Dataset.from_id() to accept full resource name

  specifically, we now allow both:

  - Dataset.from_id("dataset-1234567890")
  - Dataset.from_id("accounts/pyroworks/datasets/dataset-1234567890")

  We now strip the "accounts/<account>/datasets/" prefix when downloading the
  dataset from Fireworks. We will raise an error if the account ID in the dataset
  path does not match the API key's account.

- a2d91d4: add changelog to package

## 0.19.14

### Patch Changes

- 68fe800: stop running \_create_setup for every completions call

## 0.19.13

### Patch Changes

- 9d0d639: add attrs==23.2.0 for hex.tech

## 0.19.12

### Patch Changes

- 454f6d8: make sure we properly cache that setup is complete for LLM

## 0.19.11

### Patch Changes

- e61d36c: remove attrs constraint after some testing on hex.tech

## 0.19.10

### Patch Changes

- ddba848: export literals from fireworks

## 0.19.9

### Patch Changes

- be26985: make default epochs 1 for llm.reinforcement_step

## 0.19.8

### Patch Changes

- 8fb2d6c: add llm.reinforcement_step
- 8fb2d6c: fix handling of errors in async usage for bad gateway with HTML content
- 8fb2d6c: fix dataset.get()

## 0.19.7

### Patch Changes

- ee0a843: fix aiohttp session from being created on every request
- ee0a843: fix max_retries being implemented as max_calls
- ee0a843: accept direct_route_api_key when using direct route
- ee0a843: allow max_connections to configure maximum concurrent connections in FireworksClient
- ee0a843: add aiohttp integration for non-streaming async requests

## 0.19.6

### Patch Changes

- 46a9c2c: update name of logger to "fireworks-ai" and be less spammy by default

## 0.19.5

### Patch Changes

- 71ac70d: update another dependency to fix compatability issue with hex.tech

## 0.19.4

### Patch Changes

- 4945d8c: downgrade protobuf to 5.29.3 to work for hex

## 0.19.3

### Patch Changes

- b86a866: upgrade protobuf to 5.29.5

## 0.19.2

### Patch Changes

- ccd31af: delay imports of api_key and base_url to avoid circular imports
- ccd31af: support evaluation_dataset as Dataset or ID

## 0.19.1

### Patch Changes

- 8bba575: remove live_merge flag from LLM class
- e44d370: hotfix llm.create_supervised_fine_tuning_job

## 0.19.0

### Minor Changes

- 569e0cd: Add batch wrapper methods

### Patch Changes

- 29738bf: better defaults for connection pooling
- 25090e6: cache setup execution for high concurrency in LLM class
- 1d38e78: allow for configuration of client instance in LLM class

## 0.18.0

### Minor Changes

- 8c1cba8: force id or base_id for LLM class if on-demand or on-demand-lora

### Patch Changes

- f896c72: add perf_metrics_in_response to chat completions and completions
- ffcd302: hard delete deployments with .delete_deployment on LLM

## 0.17.21

### Patch Changes

- e730510: add responses api support

## 0.17.20

### Patch Changes

- 68ee18d: Set default log level for httpx to WARNING

## 0.17.19

### Patch Changes

- a220e6d: update evaluator creation process

## 0.17.18

### Patch Changes

- 4693100: send scale request every 10 seconds

## 0.17.17

### Patch Changes

- 2a5e439: Implements Dataset.create_evaluation_job

  - Also adds helpful functions on Dataset:
    - Dataset.from_id
    - dataset.head(as_dataset)
    - dataset.**eq**

- c1df1c5: adds nice syntax for iterating over or querying Dataset instances
- 1832cf9: always query for fireworks models
- e636bac: exit when deployment is deleted/deleting while creating/scaling up
- a4ea0d6: support usage of LLM class in a repl
- c078df4: add completions API to LLM class
- 3fdd8e8: refactor evaluator-related code into evaluator.py
- 5ecff04: added missing kwargs to chat completion functions
- 2a94873: add LLM.deployment_url for easy access to UI
- a9cef12: update generated code
- 9fab777: add Dataset.url to make it easy to print out UI link
- 9cffb20: add "from fireworks import FireworksPlatform, fw" for full access to gateway
- 92adf04: Implement dataset.preview_evaluator

## 0.17.16

### Patch Changes

- 122139b: properly set user agent in grpc library

## 0.17.15

### Patch Changes

- 72c6071: add "wait" flag to .apply() to allow for no waiting
- 8261048: add wait arg to llm.delete_deployment

## 0.17.14

### Patch Changes

- f0bf3e5: handle "model does not exist" for InvalidRequestError too since deployed model has delay between when it says deployed and when its actually available. When its not available, an error that says "model does not exist" is thrown.
- 02d6418: track sdk version

  - fixes **version** too

- 681d5c9: fix model_id not pointing to ODD if deployment_type="on-demand" is specified
- fed3520: add retries for list SFTJ
- 3039fd7: support full resource name or just id in SFTJ deletion

## 0.17.13

### Patch Changes

- f72b3bd: with_deployment_type
- 6dfcd62: syntax sugar
- 2712ac8: from_dict -> from_list
- 52c89d7: add iterable support for Dataset
- 68f09ae: add LLM.with_temperature
- cc08cf3: add LLM.list_models
- 8bd4dcf: handle existing deployed models gracefully
- f115197: allow ability to provide base deployment for loras to reuse deployments created with other display names
- fa76ec7: output_llm should return on-demand-lora deployment type if base LLM has addons enabled
- 82bcf53: don't modify min_replica_count to 0 if not specified in LLM constructor

## 0.17.12

### Patch Changes

- 155ca3a: - delete failed deployments
  - match base model in syncing SFT job
- 5c7cb95: lora working + clarified some attributes

## 0.17.11

### Patch Changes

- 1dbbd05: support custom addresses for api / gateway

## 0.17.10

### Patch Changes

- f09207a: fix dataset not syncing for llm.fine_tune

## 0.17.9

### Patch Changes

- 9288ef7: - works for Streamlit apps now
  - add RateLimitError retries
  - llm.name -> llm.deployment_name for clarity
- b4a6d0a: - fix bug with assigning autoscaling_policy
  - fix bug where scale windows were not properly reflecting provided parameters
- 5a9cc0e: less magic with llm.deployment()

## 0.17.8

### Patch Changes

- 9e01faf: add better docs for deployment_type in LLM
- d3fbfcb: use resource id for sharing link to fine-tuning job in logs
- 1d541a6: properly get jupyter notebook name for deployment display name

## 0.17.7

### Patch Changes

- 1a1eb36: fix garbage collection of Dataset causing error message
- 8aecf5e: remove greenlet dependency and related code

## 0.17.6

### Patch Changes

- a341514: must specify deployment_type now for LLM
- a341514: fix some bugs

## 0.17.5

### Patch Changes

- 912fdb8: refactor everything to be sync (TODO for async support later)

## 0.17.4

### Patch Changes

- 7aab29f: Adds nest_asyncio to run sync code inside of async context

## 0.17.3

### Patch Changes

- 2e28bea: cache list models response in the SDK itself
- bf612db: Adds llm.fine_tune / SupervisedFineTuningJob to the SDK

## 0.17.2

### Patch Changes

- af76747: expose **version** attr on fireworks import / fix "fatal: bad revision 'HEAD'"

## 0.17.1

### Patch Changes

- 440b08a: swap asyncstdlib for asyncstdlib-fw for relaxed Python version constraint

## 0.17.0

### Minor Changes

- f1ba5c8: BREAKING CHANGE:

  - Swap betterproto for betterproto-fw so fireworks-ai can be installed without
    prerelease flags and the <4.0 Python reqiurement is removed for projects that
    just specify something like >=3,9 for Python. This makes it easier to install
    with "uv" and "poetry" package managers.
  - Requires Python >= 3.9

## 0.16.4

### Patch Changes

- 162d9cb: Add Dataset class for easily creating Datasets on FW
- 5e7d555: - on-demand deployments require a label
  - you must specify deployment_type="on-demand" for serverless models to be deployed on-demand
  - better error messaging to reflect this new requirement
- 0bfdc3a: - label -> name
  - name is not required at all times, we infer name from user filename

## 0.16.3

### Patch Changes

- 1b3276a: allow more flexibility in supported Python versions

## 0.16.2

### Patch Changes

- 371f60b: Adds context cleanup for the LLM class on python process exit
- c67aeb4: add response_format type in chat completion method signature

## 0.16.1

### Patch Changes

- 65dd22a: Update README.md

## 0.16.0

### Minor Changes

- f5932cb: Added the LLM class for improved developer experience working with LLMs on Fireworks
