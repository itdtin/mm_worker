from logzero import logger

from app.api_requests import get_swap_data
from app.helpers.utils import approve, eth_price, get_random_amount, send_raw_transaction
import config

def swap(wallet, w3, params):
    try:
        if params["srcToken"] == config.ETH:
            eth_price_at_the_moment = eth_price()
            random_amount_to_use = get_random_amount(params["amountMin"], params["amountMax"])
            amount = w3.toWei(random_amount_to_use / eth_price_at_the_moment, params["srcDecimals"])
        else:
            token = w3.eth.contract(
                address=w3.toChecksumAddress(params["srcToken"]),
                abi=config.TOKEN_ABI,
            )
            amount = token.functions.balanceOf(wallet.address).call()
    except Exception as e:
        logger.log(f"Can't prepare to swap and calculate amount.\n{e}")

    try: 
        swap_data = get_swap_data(params["chainId"], params["srcToken"], amount, params["dstToken"], wallet.address)
        for i in swap_data:
            if i["trade"]:
                swap_data = i
                break
    except Exception as e:
        logger.log(f"Can't get swap data from MM.\n{e}")
 
    try:
        if params["srcToken"] != config.ETH:
            logger.log("Approving ...")
            approve(w3, token, amount, w3.toChecksumAddress(swap_data["trade"]["to"]), wallet)

        tx = {
            "data": swap_data["trade"]["data"],
            "from": w3.toChecksumAddress(swap_data["trade"]["from"]),
            "to": w3.toChecksumAddress(swap_data["trade"]["to"]),
            "value": int(swap_data["trade"]["value"]),
            "gas": swap_data["averageGas"]*6,
            "gasPrice": w3.eth.gas_price * 3,
            "nonce": w3.eth.get_transaction_count(wallet.address)

        }
        signed_txn = wallet.sign_transaction(tx)
        receipt = send_raw_transaction(w3, signed_txn)
        logger.log(f"INFO | Success swap {receipt}")
    except Exception as e:
        logger.log(f"ERROR | Can't swap.\n{e}")


