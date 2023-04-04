from logzero import logger

from app.api_requests import get_bridge_data, get_swap_data
from app.helpers.utils import send_raw_transaction
import config


def bridge(w3, wallet, chainId, src_token, src_amount, srcWei, dst_token, slippage=config.BRIDGE_SLIPPAGE, timeout=config.TIMEOUT):
    amount = w3.toWei(src_amount, srcWei)
    try:
        swap_data = get_bridge_data(chainId, src_token, amount, dst_token, wallet.address, slippage, timeout)
        for i in swap_data:
            if i["trade"]:
                swap_data = i
                break
        
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
        print(e)
        # logger.log(f"ERROR | Can't swap")

