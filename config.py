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

WAIT_BTW_PROJECT_MIN: int = 0
WAIT_BTW_PROJECT_MAX: int = 1

# Tokens
ETH: str = "0x0000000000000000000000000000000000000000"
ETH_DECIMALS: str = "ether"

USDC_DECIMALS: str = "mwei"
USDC_MAINNET: str = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
USDC_ARBITRUM: str = "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8"
USDC_OPTIMISM: str = "0x7f5c764cbc14f9669b88837ca1490cca17c31607"

USDT_DECIMALS: str = "ether"
USDT_MAINNET: str = "0xdac17f958d2ee523a2206206994597c13d831ec7"
USDT_ARBITRUM: str = "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9"
USDT_OPTIMISM: str = "0x94b008aa00579c1307b0ef2c499ad98a8ce58e58"

# Networks
MAINNET_RPC: str = (
    "https://eth-mainnet.g.alchemy.com/v2/-JUp2QTYu7vgn9j4UU5n355hWq6X4oAv"
)
MAINNET_CHAIN_ID: int = 1

ARBITRUM_RPC: str = (
    "https://arb-mainnet.g.alchemy.com/v2/aFjqA3mR0fMDkPR8lMF2QnjNQPNi9Jcm"
)
ARBITRUM_CHAIN_ID: int = 42161

OPTIMISM_RPC: str = (
    "https://opt-mainnet.g.alchemy.com/v2/0K6bMED4RlCn2DPr8tKQS8XTRMcUDKFR"
)
OPTIMISM_CHAIN_ID: int = 10

NETWORKS = {
    "ARBITRUM": {
        "GAS_LEFT": 2,
        "GAS_MULTIPLIER": 5,
        "CHAIN_ID": ARBITRUM_CHAIN_ID,
        "RPC": ARBITRUM_RPC,
        "USDC": {
            "address": USDC_ARBITRUM,
            "decimals": USDC_DECIMALS
        },
        "USDT": {
            "address": USDT_ARBITRUM,
            "decimals": USDT_DECIMALS
        },
        "ETH": {
            "address": ETH,
            "decimals": ETH_DECIMALS
        }
    },
    "OPTIMISM": {
        "GAS_LEFT": 1,
        "GAS_MULTIPLIER": 4,
        "CHAIN_ID": OPTIMISM_CHAIN_ID,
        "RPC": OPTIMISM_RPC,
        "USDC": {
            "address": USDC_OPTIMISM,
            "decimals": USDC_DECIMALS
        },
        "USDT": {
            "address": USDT_OPTIMISM,
            "decimals": USDT_DECIMALS
        },
        "ETH": {
            "address": ETH,
            "decimals": ETH_DECIMALS
        }
    },
    "MAINNET": {
        "GAS_LEFT": 2,
        "GAS_MULTIPLIER": 2,
        "CHAIN_ID": MAINNET_CHAIN_ID,
        "RPC": MAINNET_RPC,
        "USDC": {
            "address": USDC_MAINNET,
            "decimals": USDC_DECIMALS
        },
        "USDT": {
            "address": USDT_MAINNET,
            "decimals": USDT_DECIMALS
        },
        "ETH": {
            "address": ETH,
            "decimals": ETH_DECIMALS
        }
    }
}
