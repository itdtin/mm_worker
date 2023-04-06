import dotenv
from app.helpers.abis import TOKEN_ABI

dotenv.load_dotenv()

to_run = {
    "MAINNET": {
        "swap": False,
        "bridge": False
    },
    "ARBITRUM": {
        "swap": True,
        "bridge": True
    },
    "BSC": {
        "swap": True,
        "bridge": True
    },
    "OPTIMISM": {
        "swap": True,
        "bridge": True
    },
}

ATTEMTS_TO_NODE_REQUEST = 9
ATTEMTS_TO_API_REQUEST = 9

BRIDGE_BALANCE_WAIT_TIME: int = 2000 # 2000 seconds

# Swap
SWAP_SLIPPAGE: int = 5 # Metamask default
BRIDGE_SLIPPAGE: int = 5 # Metamask default
TIMEOUT: int = 10000 # Metamask default

# Wait
WAIT_BTW_WALLET_MIN: int = 1
WAIT_BTW_WALLET_MAX: int = 2

WAIT_BTW_PROJECT_MIN: int = 4
WAIT_BTW_PROJECT_MAX: int = 7

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
        "GAS_LEFT": 4,
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
        "BAL": {
            "address": "0x040d1EdC9569d4Bab2D15287Dc5A4F10F56a56B8",
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
        "USDT": {
            "address": "0x55d398326f99059ff775485246999027b3197955",
            "decimals": ETH_DECIMALS
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
