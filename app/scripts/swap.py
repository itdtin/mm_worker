import random
from time import sleep
from logzero import logger
from web3 import Web3

from app.api_requests import get_swap_data
from app.helpers.utils import approve, eth_price, get_random_amount, send_raw_transaction
import config

def swap(wallet, params):
    srcChain = config.NETWORKS.get(params.get("srcChain"))
    srcToken = srcChain.get(params.get("srcToken"))
    srcTokenAddress = srcToken.get("address")

    dstChain = config.NETWORKS.get(params.get("dstChain"))
    dstToken = dstChain.get(params.get("dstToken"))
    dstTokenAddress = dstToken.get("address")

    gas_multiplier = srcChain.get("GAS_MULTIPLIER")
    w3 = Web3(Web3.HTTPProvider(srcChain.get("RPC")))
    try:
        if srcTokenAddress == config.ETH:
            balance_wei = w3.eth.get_balance(wallet.address)
        else:
            token = w3.eth.contract(
                address=w3.toChecksumAddress(srcTokenAddress),
                abi=config.TOKEN_ABI,
            )
            balance_wei = token.functions.balanceOf(wallet.address).call()
        amount = int(balance_wei / 100 * params["amountP"])
    except Exception as e:
        logger.error(f"ERROR | Can't prepare to swap and calculate amount.\n{e}")
        return False
    sleep(3)
    try: 
        swap_data = get_swap_data(srcChain.get("CHAIN_ID"), srcTokenAddress, amount, dstTokenAddress, wallet.address, config.SWAP_SLIPPAGE, config.TIMEOUT)
        for i in swap_data:
            if i["trade"]:
                swap_data = i
                break
    except Exception as e:
        logger.error(f"ERROR | Can't get swap data from MM.\n{e}")
        return False
    try:
        if srcTokenAddress != config.ETH:
            logger.info("Approving ...")
            approve(w3, token, w3.toChecksumAddress(swap_data["trade"]["to"]), amount, wallet)
            sleep(3)
        logger.info("Swapping ...")
        tryNum = 0
        while True:
            gas_multiplier += 1
            try:
                tx = {
                    "data": swap_data["trade"]["data"],
                    "from": w3.toChecksumAddress(swap_data["trade"]["from"]),
                    "to": w3.toChecksumAddress(swap_data["trade"]["to"]),
                    "value": int(swap_data["trade"]["value"]),
                    "gas": swap_data["averageGas"] * gas_multiplier,
                    "gasPrice": w3.eth.gas_price,
                    "nonce": w3.eth.get_transaction_count(wallet.address),
                    "chainId": srcChain["CHAIN_ID"]

                }
                signed_txn = wallet.sign_transaction(tx)
                receipt = send_raw_transaction(w3, signed_txn)
                logger.info(f"INFO | Success swap {receipt}")
                return receipt
            except Exception as e:
                tryNum += 1
                logger.error(f"ERROR | while swapping - attempt {tryNum}.\n{e}")
                if tryNum > config.ATTEMTS_TO_NODE_REQUEST:
                    logger.error(f"ERROR | while swapping.\n{e}")
                    return False
                sleep(10)
    except Exception as e:
        logger.error(f"ERROR | Can't swap.\n{e}")
        return False

