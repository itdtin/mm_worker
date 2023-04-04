from config import *
# Flows
PROJECTS = {
    "ARBITRUM": [
        {
            "script": "swap",
            "srcChain": "ARBITRUM",
            "dstChain": "ARBITRUM",
            "srcToken": "ETH",
            "dstToken": "USDC",
            "amountP": 95, # 95%
        },
        {
            "script": "swap",
            "srcChain": "ARBITRUM",
            "dstChain": "ARBITRUM",
            "srcToken": "USDC",
            "dstToken": "ETH",
            "amountP": 100
        },
        {
            "script": "bridge",
            "srcChain": "ARBITRUM",
            "dstChain": "OPTIMISM",
            "srcToken": "ETH",
            "dstToken": "ETH",
            "amountP": 100
        },
    ]
}
