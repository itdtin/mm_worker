from config import *
# Flows
PROJECTS = {
    "MAINNET": [    
        {
            "script": "swap",
            "srcChain": "MAINNET",
            "dstChain": "MAINNET",
            "srcToken": "ETH",
            "dstToken": "LINK",
            "amountP": 90, # 95%
        },
        {
            "script": "swap",
            "srcChain": "MAINNET",
            "dstChain": "MAINNET",
            "srcToken": "LINK",
            "dstToken": "GRT",
            "amountP": 100
        },
        {
            "script": "swap",
            "srcChain": "MAINNET",
            "dstChain": "MAINNET",
            "srcToken": "GRT",
            "dstToken": "ETH",
            "amountP": 100
        },
        {
            "script": "bridge",
            "srcChain": "MAINNET",
            "dstChain": "ARBITRUM",
            "srcToken": "ETH",
            "dstToken": "ETH",
            "amountP": 100
        },
    ],
    "ARBITRUM": [
        {
            "script": "swap",
            "srcChain": "ARBITRUM",
            "dstChain": "ARBITRUM",
            "srcToken": "ETH",
            "dstToken": "BAL",
            "amountP": 92, # 92%
        },
        {
            "script": "swap",
            "srcChain": "ARBITRUM",
            "dstChain": "ARBITRUM",
            "srcToken": "BAL",
            "dstToken": "USDC",
            "amountP": 99.9999
        },
        {
            "script": "bridge",
            "srcChain": "ARBITRUM",
            "dstChain": "BSC",
            "srcToken": "USDC",
            "dstToken": "USDC",
            "amountP": 100
        },
    ],
    "BSC": [
        {
            "script": "swap",
            "srcChain": "BSC",
            "dstChain": "BSC",
            "srcToken": "USDC",
            "dstToken": "USDT",
            "amountP": 99.9999, 
        },
        {
            "script": "swap",
            "srcChain": "BSC",
            "dstChain": "BSC",
            "srcToken": "USDT",
            "dstToken": "USDC",
            "amountP": 99.9999
        },
        {
            "script": "bridge",
            "srcChain": "BSC",
            "dstChain": "OPTIMISM",
            "srcToken": "USDC",
            "dstToken": "USDC",
            "amountP": 99.999
        },
    ],
    "OPTIMISM": [
        {
            "script": "swap",
            "srcChain": "OPTIMISM",
            "dstChain": "OPTIMISM",
            "srcToken": "USDC",
            "dstToken": "OP",
            "amountP": 100, # 100%
        },
        {
            "script": "swap",
            "srcChain": "OPTIMISM",
            "dstChain": "OPTIMISM",
            "srcToken": "OP",
            "dstToken": "ETH",
            "amountP": 99.9999, # OP bad calculation cause 99.99
        },
        {
            "script": "bridge",
            "srcChain": "OPTIMISM",
            "dstChain": "ARBITRUM",
            "srcToken": "ETH",
            "dstToken": "ETH",
            "amountP": 100
        },
    ]
}
