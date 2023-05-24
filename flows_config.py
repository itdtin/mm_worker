from config import *
# Flows
PROJECTS = {
    "BSC": [
        {
            "script": "swap",
            "srcChain": "BSC",
            "dstChain": "BSC",
            "srcToken": "USDT",
            "dstToken": "USDC",
            "amountP": 99.9999, # amount in percent
        },
        {
            "script": "swap",
            "srcChain": "BSC",
            "dstChain": "BSC",
            "srcToken": "USDC",
            "dstToken": "USDT",
            "amountP": 99.9999
        },
        {
            "script": "bridge",
            "srcChain": "BSC",
            "dstChain": "POLYGON",
            "srcToken": "USDT",
            "dstToken": "USDT",
            "amountP": 99.999
        },
    ],
    "POLYGON": [
        {
            "script": "bridge",
            "srcChain": "POLYGON",
            "dstChain": "BSC",
            "srcToken": "USDT",
            "dstToken": "USDT",
            "amountP": 99.9999, # amount in percent
        },
        {
            "script": "swap",
            "srcChain": "BSC",
            "dstChain": "BSC",
            "srcToken": "USDT",
            "dstToken": "USDC",
            "amountP": 99.9999
        },
    ],
}
