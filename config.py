import dotenv
from app.helpers.abis import TOKEN_ABI

dotenv.load_dotenv()

ATTEMTS_TO_NODE_REQUEST = 9
ATTEMTS_TO_API_REQUEST = 9

# Swap
SWAP_SLIPPAGE: int = 3
BRIDGE_SLIPPAGE: int = 5
TIMEOUT: int = 10000

# Wait
WAIT_BTW_WALLET_MIN: int = 1
WAIT_BTW_WALLET_MAX: int = 2

WAIT_BTW_PROJECT_MIN: int = 2
WAIT_BTW_PROJECT_MAX: int = 4

# Tokens
ETH: str = "0x0000000000000000000000000000000000000000"
ETH_DECIMALS: str = "ether"

USDC_DECIMALS: str = "mwei"


# Networks
MAINNET_RPC: str = "https://eth-mainnet.g.alchemy.com/v2/-JUp2QTYu7vgn9j4UU5n355hWq6X4oAv"
MAINNET_CHAIN_ID: int = 1

ARBITRUM_RPC: str = "https://arb-mainnet.g.alchemy.com/v2/aFjqA3mR0fMDkPR8lMF2QnjNQPNi9Jcm"
ARBITRUM_CHAIN_ID: int = 42161

OPTIMISM_RPC: str = "https://opt-mainnet.g.alchemy.com/v2/0K6bMED4RlCn2DPr8tKQS8XTRMcUDKFR"
OPTIMISM_CHAIN_ID: int = 10

POLYGON_RPC: str = "https://polygon-mainnet.g.alchemy.com/v2/ncSSy-j4i1T3hcN5hFCtEsyghpLCw_0p"
POLYGON_CHAIN_ID: int = 137

AVAX_RPC: str = "https://avalanche-mainnet.infura.io/v3/ca0d7f3c70f84e22ab29e5a74b329a3a"
AVAX_CHAIN_ID: int = 43114

BSC_RPC: str = "https://alien-nameless-breeze.bsc.quiknode.pro/bdecd2a7ddc4f6d270d26a9cd5c1b4f3c120ff53/"
BSC_CHAIN_ID: int = 56

NETWORKS = {
    "MAINNET": {
        "GAS_LEFT": 10,
        "GAS_MULTIPLIER": 1,
        "CHAIN_ID": MAINNET_CHAIN_ID,
        "RPC": MAINNET_RPC,
        "USDC": {
            "address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "decimals": USDC_DECIMALS
        },
        "USDT": {
            "address": "0xdac17f958d2ee523a2206206994597c13d831ec7",
            "decimals": ETH_DECIMALS
        },
        "ETH": {
            "address": ETH,
            "decimals": ETH_DECIMALS
        },
        "LINK": {
            "address": "0x514910771af9ca656af840dff83e8264ecf986ca",
            "decimals": ETH_DECIMALS
        },
        "GRT": {
            "address": "0xc944e90c64b2c07662a292be6244bdf05cda44a7",
            "decimals": ETH_DECIMALS
        }
    },
    "ARBITRUM": {
        "GAS_LEFT": 2,
        "GAS_MULTIPLIER": 4,
        "CHAIN_ID": ARBITRUM_CHAIN_ID,
        "RPC": ARBITRUM_RPC,
        "USDC": {
            "address": "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8",
            "decimals": USDC_DECIMALS
        },
        "USDT": {
            "address": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
            "decimals": ETH_DECIMALS
        },
        "ETH": {
            "address": ETH,
            "decimals": ETH_DECIMALS
        },
        "COMP": {
            "address": "0x354A6dA3fcde098F8389cad84b0182725c6C91dE",
            "decimals": ETH_DECIMALS
        }
    },
    "BSC": {
        "GAS_LEFT": 1,
        "GAS_MULTIPLIER": 1,
        "CHAIN_ID": BSC_CHAIN_ID,
        "RPC": BSC_RPC,
        "USDC": {
            "address": "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d",
            "decimals": USDC_DECIMALS
        },
        "ADA": {
            "address": "0x3ee2200efb3400fabb9aacf31297cbdd1d435d47",
            "decimals": ETH_DECIMALS
        },
        "DAI": {
            "address": "0x1af3f329e8be154074d8769d1ffa4ee058b1dbc3",
            "decimals": ETH_DECIMALS
        }
    },
    "AVAX": {
        "GAS_LEFT": 1,
        "GAS_MULTIPLIER": 3,
        "CHAIN_ID": AVAX_CHAIN_ID,
        "RPC": AVAX_RPC,
        "USDC": {
            "address": "0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E",
            "decimals": USDC_DECIMALS
        },
        "USDCE": {
            "address": "0xa7d7079b0fead91f3e65f86e8915cb59c1a4c664",
            "decimals": USDC_DECIMALS
        },
        "USDT": {
            "address": "0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7",
            "decimals": ETH_DECIMALS
        },
        "AVAX": {
            "address": ETH,
            "decimals": ETH_DECIMALS
        },
        "DAI": {
            "address": "0xd586E7F844cEa2F87f50152665BCbc2C279D8d70",
            "decimals": ETH_DECIMALS
        }
    },
    "POLYGON": {
        "GAS_LEFT": 1,
        "GAS_MULTIPLIER": 3,
        "CHAIN_ID": POLYGON_CHAIN_ID,
        "RPC": POLYGON_RPC,
        "USDT": {
            "address": "0xc2132d05d31c914a87c6611c10748aeb04b58e8f",
            "decimals": ETH_DECIMALS
        },
        "UNI": {
            "address": "0xb33eaad8d922b1083446dc23f610c2567fb5180f",
            "decimals": ETH_DECIMALS
        },
        "USDC": {
            "address": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174",
            "decimals": USDC_DECIMALS
        }
    },
    "OPTIMISM": {
        "GAS_LEFT": 1,
        "GAS_MULTIPLIER": 4,
        "CHAIN_ID": OPTIMISM_CHAIN_ID,
        "RPC": OPTIMISM_RPC,
        "USDC": {
            "address": "0x7f5c764cbc14f9669b88837ca1490cca17c31607",
            "decimals": USDC_DECIMALS
        },
        "USDT": {
            "address": "0x94b008aa00579c1307b0ef2c499ad98a8ce58e58",
            "decimals": ETH_DECIMALS
        },
        "ETH": {
            "address": ETH,
            "decimals": ETH_DECIMALS
        },
        "OP": {
            "address": "0x4200000000000000000000000000000000000042",
            "decimals": ETH_DECIMALS
        }
    },

}
