from config import *
# Flows
PROJECTS = {
    # "arb_sw_eth": {
    #     "script": "swap",
    #     "srcChain": "ARBITRUM",
    #     "dstChain": "ARBITRUM",
    #     "srcToken": "ETH",
    #     "dstToken": "USDC",
    #     "amountP": 95, # 95%
    # },
    # "arb_sw_token": {
    #     "script": "swap",
    #     "srcChain": "ARBITRUM",
    #     "dstChain": "ARBITRUM",
    #     "srcToken": "USDC",
    #     "dstToken": "ETH",
    #     "amountP": 100
    # },
    "arb_op_br": {
        "script": "bridge",
        "srcChain": "ARBITRUM",
        "dstChain": "OPTIMISM",
        "srcToken": "ETH",
        "dstToken": "ETH",
        "amountP": 100
    },
}
