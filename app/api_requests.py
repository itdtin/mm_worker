import requests

import time

import config
from logzero import logger


def eth_price():
    url = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD"
    result = get(url)
    return result.json()["USD"]


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



def get_swap_data():
    url = "https://swap.metaswap.codefi.network/networks/42161/trades?sourceAmount=10000000000000000&sourceToken=0x0000000000000000000000000000000000000000&destinationToken=0x11cdb42b0eb46d95f990bedd4695a6e3fa034978&slippage=3&walletAddress=0xc17e5dec5a1f32a947d4456906fe53079215f76b&timeout=10000&enableDirectWrapping=true&includeRoute=true"

def get_bridge_data():
    pass