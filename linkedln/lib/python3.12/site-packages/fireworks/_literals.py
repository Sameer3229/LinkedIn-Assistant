from typing import Literal

ReinforcementAcceleratorTypeLiteral = Literal[
    "NVIDIA_A100_80GB",
    "NVIDIA_H100_80GB",
    "NVIDIA_H200_141GB",
]

AcceleratorTypeLiteral = Literal[
    "ACCELERATOR_TYPE_UNSPECIFIED",
    "NVIDIA_A100_80GB",
    "NVIDIA_H100_80GB",
    "AMD_MI300X_192GB",
    "NVIDIA_A10G_24GB",
    "NVIDIA_A100_40GB",
    "NVIDIA_L4_24GB",
    "NVIDIA_H200_141GB",
    "NVIDIA_B200_180GB",
]


RegionLiteral = Literal[
    "REGION_UNSPECIFIED",
    "US_IOWA_1",
    "US_VIRGINIA_1",
    "US_VIRGINIA_2",
    "US_ILLINOIS_1",
    "AP_TOKYO_1",
    "EU_LONDON_1",
    "US_ARIZONA_1",
    "US_TEXAS_1",
    "US_ILLINOIS_2",
    "EU_FRANKFURT_1",
    "US_TEXAS_2",
    "EU_PARIS_1",
    "EU_HELSINKI_1",
    "US_NEVADA_1",
    "EU_ICELAND_1",
    "EU_ICELAND_2",
    "US_WASHINGTON_1",
    "US_WASHINGTON_2",
    "EU_ICELAND_DEV_1",
]

MultiRegionLiteral = Literal["MULTI_REGION_UNSPECIFIED", "GLOBAL", "US"]


ReasoningEffort = Literal["low", "medium", "high"]

"""
serverless: always use serverless, if not available, raise an error
on-demand: always use on-demand. For LoRA addons, this will create a new on-demand deployment for the LoRA model without addons enabled (for performance reasons).
auto: use serverless if available, otherwise use on-demand. For LoRA addons, this will create a new on-demand deployment for the LoRA model with addons enabled.
on-demand-lora: always use on-demand (even if serverless is available). For LoRA addons, this will create a new on-demand deployment for the LoRA model with addons enabled.
"""
DeploymentTypeLiteral = Literal["serverless", "on-demand", "auto", "on-demand-lora"]


DeploymentStrategyLiteral = Literal["serverless", "on-demand", "serverless-lora", "on-demand-lora"]

PrecisionLiteral = Literal[
    "FP16",
    "FP8",
    "FP8_MM",
    "FP8_AR",
    "FP8_MM_KV_ATTN",
    "FP8_KV",
    "FP8_MM_V2",
    "FP8_V2",
    "FP8_MM_KV_ATTN_V2",
    "NF4",
]

DirectRouteTypeLiteral = Literal["INTERNET", "GCP_PRIVATE_SERVICE_CONNECT", "AWS_PRIVATELINK"]


WeightPrecisionLiteral = Literal["WEIGHT_PRECISION_UNSPECIFIED", "BFLOAT16", "INT8", "NF4"]
