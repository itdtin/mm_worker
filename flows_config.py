from config import *
# Flows
PROJECTS = {
    "arb_sw_eth": {
        "script": "swap",
        "srcChain": "ARBITRUM",
        "dstChain": "ARBITRUM",
        "srcToken": "ETH",
        "dstToken": "USDC",
        "amountMin": 12.1, # Swap in params in usd
        "amountMax": 13.1,
    },
    "arb_sw_token": {
        "script": "swap",
        "srcChain": "ARBITRUM",
        "dstChain": "ARBITRUM",
        "srcToken": "USDC",
        "dstToken": "ETH",
        "amountMin": 12.1, # Swap in params in usd
        "amountMax": 13.1,
    }
}
