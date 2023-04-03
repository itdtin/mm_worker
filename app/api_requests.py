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
    pass 

def get_bridge_data():
    pass