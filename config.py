import dotenv
from app.projects.abis import (
    TOKEN_ABI,
    GLP_REWARD_ROUTER_ABI,
    GMX_ROUTER_ABI,
    GMX_POSITION_ROUTER_ABI,
    MAINNET_ARBI_BRIDGE_ABI,
    SUSHI_ROUTER_ABI,
    DAI_ABI,
)


dotenv.load_dotenv()

bridge_to_nova = False
run_nova_projects = True
bridge_nova_to_arbitrum = False
run_arbi_projects = False

GLP_MIN: float = 1.5
GLP_MAX: float = 1.7

GMX_MIN: float = 12.1
GMX_MAX: float = 13.2

MAGIC_MIN: float = 2.1
MAGIC_MAX: float = 2.7

USDC_SWAP_NOVA_SUSHI_MIN: float = 1.5
USDC_SWAP_NOVA_SUSHI_MAX: float = 1.9

DAI_SWAP_NOVA_SUSHI_MIN: float = 1.5
DAI_SWAP_NOVA_SUSHI_MAX: float = 1.9

USDC_SWAP_NOVA_ARBSWAP_MIN: float = 1.5
USDC_SWAP_NOVA_ARBSWAP_MAX: float = 1.9

DAI_SWAP_NOVA_ARBSWAP_MIN: float = 1.5
DAI_SWAP_NOVA_ARBSWAP_MAX: float = 1.9

USDC_DAI_LIQUIDITY_SUSHI_MIN: float = 3.1
USDC_DAI_LIQUIDITY_SUSHI_MAX: float = 3.8

USDC_DAI_LIQUIDITY_ARBSWAP_MIN: float = 2.6
USDC_DAI_LIQUIDITY_ARBSWAP_MAX: float = 2.9

WAIT_BTW_WALLET_MIN: int = 3
WAIT_BTW_WALLET_MAX: int = 5

WAIT_BTW_PROJECT_MIN: int = 3
WAIT_BTW_PROJECT_MAX: int = 5

NOVA_ARBI_BRIDGE_TX_COUNT: int = 3

ARBI_PROJECTS = ["glp", "gmx", "magic"]
NOVA_PROJECTS = [
    "dai_nova_sushi",
    "usdc_nova_sushi",
    "sushi_liquidity_nova",
    "dai_nova_arbswap",
    "usdc_nova_arbswap",
    "arbswap_liquidity_nova",
]

DEFAULT_FEE_PER_PROJ: float = 0.8
FEE_OFFSET: float = 0.2
SUSHI_SLIPPAGE: float = 0.03
SUSHI_LIQUIDITY_SLIPAGE: float = 0.03

RANDOM_MIN: float = 0.00000000001
RANDOM_MAX: float = 0.00000003

ATTEMTS_TO_NODE_REQUEST = 9
ATTEMTS_TO_API_REQUEST = 9
ATTEMTS_SWAP = 9
ATTEMTS_BRIDGE = 3

MAINNET_RPC: str = (
    "https://eth-mainnet.g.alchemy.com/v2/YfPn32Pq_71oNoxd3UkIMqqHehGjjdwQ"
)
ARBITRUM_RPC: str = (
    "https://arb-mainnet.g.alchemy.com/v2/aFjqA3mR0fMDkPR8lMF2QnjNQPNi9Jcm"
)
ARBITRUM_NOVA_RPC: str = "https://nova.arbitrum.io/rpc"
SLIPPAGE: int = 3

# Bridge
MAINNET_ARBI_NOVA_BRIDGE: str = "0xc4448b71118c9071Bcb9734A0EAc55D18A153949"

# Tokens
ETH: str = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"
ETH_DECIMALS: str = "ether"

MAGIC_ARBITRUM: str = "0x539bdE0d7Dbd336b79148AA742883198BBF60342"
GMX_ARBITRUM: str = "0xfc5a1a6eb076a2c7ad06ed22c90d7e710e35ad0a"

USDC_DECIMALS: str = "mwei"
USDC_ARBITRUM: str = "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8"
USDC_ARBITUM_NOVA: str = "0x750ba8b76187092B0D1E87E28daaf484d1b5273b"
DAI_ARBITRUM_NOVA: str = "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1"

# Protocols
GLP_REWARD_ROUTER: str = "0xb95db5b167d75e6d04227cfffa61069348d271f5"
GMX_ROUTER: str = "0xabbc5f99639c9b6bcb58544ddf04efa6802f4064"
GMX_POSITION_ROUTER: str = "0xb87a436b93ffe9d75c5cfa7bacfff96430b09868"
GMX_POSITION_MULTIPLOCATOR: float = 1.02

SUSHI_NOVA_ROUTER: str = "0x1b02da8cb0d097eb8d57a175b88c7d8b47997506"
ARBSWAP_NOVA_ROUTER: str = "0xee01c0cd76354c383b8c7b4e65ea88d00b06f36f"
ORBITER_NOVA_BRIDGE: str = "0x80c67432656d59144ceff962e8faf8926599bcf8"
ORBITER_MIN: float = 0.0057
ORBITER_END_AMOUNT: str = "0009002"

PROJECTS = {
    "glp": {
        "token": "",
        "amountMin": GLP_MIN,
        "amountMax": GLP_MAX,
        "contract": [GLP_REWARD_ROUTER, GLP_REWARD_ROUTER_ABI],
    },
    "gmx": {
        "token": "",
        "amountMin": GMX_MIN,
        "amountMax": GMX_MAX,
        "contract": [
            [GMX_ROUTER, GMX_ROUTER_ABI],
            [GMX_POSITION_ROUTER, GMX_POSITION_ROUTER_ABI],
        ],
    },
    "magic": {
        "token": MAGIC_ARBITRUM,
        "amountMin": MAGIC_MIN,
        "amountMax": MAGIC_MAX,
    },
    "usdc_nova_sushi": {
        "token": USDC_ARBITUM_NOVA,
        "amountMin": USDC_SWAP_NOVA_SUSHI_MIN,
        "amountMax": USDC_SWAP_NOVA_SUSHI_MAX,
    },
    "dai_nova_sushi": {
        "token": DAI_ARBITRUM_NOVA,
        "amountMin": DAI_SWAP_NOVA_SUSHI_MIN,
        "amountMax": DAI_SWAP_NOVA_SUSHI_MAX,
    },
    "sushi_liquidity_nova": {
        "dai": DAI_ARBITRUM_NOVA,
        "usdc": USDC_ARBITUM_NOVA,
        "amountMin": USDC_DAI_LIQUIDITY_SUSHI_MIN,
        "amountMax": USDC_DAI_LIQUIDITY_SUSHI_MAX,
    },
    "usdc_nova_arbswap": {
        "token": USDC_ARBITUM_NOVA,
        "amountMin": USDC_SWAP_NOVA_ARBSWAP_MIN,
        "amountMax": USDC_SWAP_NOVA_ARBSWAP_MAX,
    },
    "dai_nova_arbswap": {
        "token": DAI_ARBITRUM_NOVA,
        "amountMin": DAI_SWAP_NOVA_ARBSWAP_MIN,
        "amountMax": DAI_SWAP_NOVA_ARBSWAP_MAX,
    },
    "arbswap_liquidity_nova": {
        "dai": DAI_ARBITRUM_NOVA,
        "usdc": USDC_ARBITUM_NOVA,
        "amountMin": USDC_DAI_LIQUIDITY_ARBSWAP_MIN,
        "amountMax": USDC_DAI_LIQUIDITY_ARBSWAP_MAX,
    },
}
