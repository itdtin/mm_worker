import random
from time import sleep
from logzero import logger
from web3 import Web3

from app.api_requests import get_bridge_data, get_swap_data
from app.helpers.utils import approve, eth_price, send_raw_transaction, wait_balance_after_bridge
import config


def bridge(wallet, params, wait_balance=True):
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
            balance_wei = int(w3.eth.get_balance(wallet.address) - w3.toWei(srcChain["GAS_LEFT"] / eth_price(), config.ETH_DECIMALS))
        else:
            token = w3.eth.contract(
                address=w3.toChecksumAddress(srcTokenAddress),
                abi=config.TOKEN_ABI,
            )
            balance_wei = token.functions.balanceOf(wallet.address).call()
        amount = int(balance_wei / 100 * params["amountP"])
    except Exception as e:
        logger.error(f"ERROR | Can't prepare to swap and calculate amount.\n{e}")
    sleep(3)
    
    try:
        bridge_data = get_bridge_data(
            wallet.address,
            srcChain.get("CHAIN_ID"),
            dstChain.get("CHAIN_ID"),
            srcTokenAddress,
            dstTokenAddress,
            amount,
            config.BRIDGE_SLIPPAGE,
        )
        for i in bridge_data:
            if i["trade"]:
                bridge_data = i
                break
    except Exception as e:
        logger.error(f"ERROR | Can't get swap data from MM.\n{e}")

    try:
        if srcTokenAddress != config.ETH:
            logger.info("Approving ...")
            approve(
                w3,
                token,
                w3.toChecksumAddress(bridge_data["trade"]["to"]),
                amount,
                wallet,
            )
            sleep(3)

        logger.info("Bridging ...")
        tryNum = 0
        while True:
            try:
                tx = {
                    "data": bridge_data["trade"]["data"],
                    "from": w3.toChecksumAddress(bridge_data["trade"]["from"]),
                    "to": w3.toChecksumAddress(bridge_data["trade"]["to"]),
                    "value": bridge_data["trade"]["value"],
                    "gas": bridge_data["trade"]["gasLimit"] * gas_multiplier,
                    "gasPrice": w3.eth.gas_price,
                    "nonce": w3.eth.get_transaction_count(wallet.address),
                    "chainId": srcChain["CHAIN_ID"]
                }
                gas_multiplier += 1
                signed_txn = wallet.sign_transaction(tx)
                receipt = send_raw_transaction(w3, signed_txn)
                logger.info(f"INFO | Success bridge {receipt}")
                if wait_balance:
                    wait_balance_after_bridge(wallet.address, dstToken, dstChain)
                return receipt
            except Exception as e:
                tryNum += 1
                logger.error(f"ERROR | while bridging - attempt {tryNum}.\n{e}")
                if tryNum > config.ATTEMTS_TO_NODE_REQUEST:
                    logger.error(f"ERROR | while bridging.\n{e}")
                    return False
                sleep(5)

    except Exception as e:
        logger.error(f"ERROR | Can't bridge.\n{e}")
