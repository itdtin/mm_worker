import requests

import time

import config
from logzero import logger


def get(url, headers=None, params=None):
    if params is None:
        params = {}
    if headers is None:
        headers = {}
    tryNum = 0
    while True:
        try:
            r = requests.get(url, headers=headers, params=params)
            return r
        except Exception as e:
            tryNum += 1
            if tryNum > config.ATTEMTS_TO_API_REQUEST:
                logger.error(f"ERROR | Can't get response from {url}.\n{e}")
                raise e
            time.sleep(10)


def get_swap_data(chainId, src_token, src_amount, dst_token, wallet_address, slippage, timeout):
    url = f"https://swap.metaswap.codefi.network/networks/{chainId}/trades?sourceAmount={src_amount}&sourceToken={src_token}&destinationToken={dst_token}&slippage={slippage}&walletAddress={wallet_address}&timeout={timeout}&enableDirectWrapping=true&includeRoute=true"
    return get(url).json()


def get_bridge_data(wallet_address, src_chain_id, dst_chain_id, src_token, dst_token, src_amount_wei, slippage):
    url1 = f"https://bridge.metaswap.codefi.network/getQuote?walletAddress={wallet_address}&srcChainId={src_chain_id}&destChainId={dst_chain_id}&srcTokenAddress={src_token}&destTokenAddress={dst_token}&srcTokenAmount={src_amount_wei}&slippage={slippage}&aggIds=socket,lifi&insufficientBal=true"
    url2 = f"https://bridge.metaswap.codefi.network/getQuote?walletAddress={wallet_address}&srcChainId={src_chain_id}&destChainId={dst_chain_id}&srcTokenAddress={src_token}&destTokenAddress={dst_token}&srcTokenAmount={src_amount_wei}&slippage={slippage}&aggIds=socket,lifi&insufficientBal=false"
    data1 = get(url1).json()
    data2 = get(url2).json()
    data = data1 + data2
    return data