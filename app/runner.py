import random
import time
from pathlib import Path
import os

from queue import Queue
from web3 import Account, Web3
from logzero import logger

import config
from app.arbi_bridge import arbi_bridge
from app.orbiter_bridge_ETH import orbiter_bridge_ETH
from app.projects.flow import projects
from app.utils import get_random_amount, eth_price


class Runner:
    w3_mainnet = Web3(Web3.HTTPProvider(config.MAINNET_RPC))
    w3_nova = Web3(Web3.HTTPProvider(config.ARBITRUM_NOVA_RPC))
    w3_arbi = Web3(Web3.HTTPProvider(config.ARBITRUM_RPC))

    def __init__(self, wallets_path):
        self.wallets = self.import_wallets(wallets_path)
        self.projects = {func.__name__: func for func in projects()}
        self.wallets_queue = Queue()
        for wallet in self.wallets:
            self.wallets_queue.put(wallet)

        self.wait_wlt = (config.WAIT_BTW_WALLET_MIN, config.WAIT_BTW_WALLET_MAX)
        self.wait_projects = (config.WAIT_BTW_PROJECT_MIN, config.WAIT_BTW_PROJECT_MAX)

    def do_work(self):
        print("do work")
        results = {}
        to_run = self.define_projects_to_run_params()

        while self.wallets_queue.qsize():
            wallet = self.wallets_queue.get()
            results[wallet.address] = {}
            self.run_projects_in_order(wallet, to_run)
            self.make_pause_btw_wlt()

    def run_projects_in_order(self, wallet, to_run_projects):
        if config.bridge_to_nova:
            arb_bridged = arbi_bridge(self.w3_mainnet, self.w3_nova, wallet)
        else:
            logger.info(f"INFO | Arbi Bridge | Turned OFF")
            arb_bridged = True

        if config.run_nova_projects and arb_bridged:
            nova_order = random.sample(config.NOVA_PROJECTS, len(config.NOVA_PROJECTS))
            for proj_name in nova_order:
                self.run_project(wallet, proj_name, to_run_projects[proj_name])
                self.make_pause_btw_projects()

        if config.bridge_nova_to_arbitrum:
            orbiter_bridged = False
            balance_ = self.w3_nova.eth.get_balance(wallet.address)
            for_each_amount = float(
                self.w3_nova.fromWei(balance_, config.ETH_DECIMALS)
            ) / (3 + config.SUSHI_SLIPPAGE)
            for i in range(config.NOVA_ARBI_BRIDGE_TX_COUNT):
                orbiter_bridged = orbiter_bridge_ETH(
                    self.w3_nova, self.w3_arbi, wallet, for_each_amount
                )
        else:
            orbiter_bridged = True

        if config.run_arbi_projects and orbiter_bridged:
            arbi_order = random.sample(config.ARBI_PROJECTS, len(config.ARBI_PROJECTS))
            for proj_name in arbi_order:
                self.run_project(wallet, proj_name, to_run_projects[proj_name])
                self.make_pause_btw_projects()

    def run_project(self, wallet, project_name: str, run_args=None):
        logger.info(f"Starting {project_name}")
        if not run_args:
            run_args = []
        args = [wallet] + run_args
        amounts = run_args[-1]
        amounts[1] = amounts[1] - get_random_amount(
            config.RANDOM_MIN, config.RANDOM_MAX, 15, 18
        )
        run_args[-1] = amounts
        quest_flow = self.projects.get(project_name)
        if quest_flow:
            result = quest_flow(*args)
            return result

    def import_wallets(self, file_name: str):
        accounts = []
        if os.path.exists(file_name):
            with Path(file_name).open() as file:
                for line in file.readlines():
                    key_ = line.replace("\n", "")
                    try:
                        acc = Account.from_key(key_)
                        accounts.append(acc)
                    except Exception as e:
                        logger.error("ERROR| Incorrect PK")
            if len(accounts) > 0:
                logger.info("INFO | Wallets has been loaded")
            return accounts
        else:
            logger.error(" ERROR | Incorrect path to wallets.txt")
        return []

    def make_pause_btw_wlt(self) -> None:
        self.make_pause(self.wait_wlt)

    def make_pause_btw_projects(self) -> None:
        self.make_pause(self.wait_projects)

    @staticmethod
    def make_pause(wait_type):
        counter = random.randint(*wait_type)
        logger.info(f"INFO | Pause ...{wait_type}")
        step = 0.1
        while counter > 0:
            time.sleep(step)
            counter -= step

    def define_projects_to_run_params(self):
        to_run_params = {}
        for project_name, proj_params in config.PROJECTS.items():
            eth_price_at_the_moment = eth_price()
            random_amount_to_use = get_random_amount(
                proj_params["amountMin"],
                proj_params["amountMax"],
            )

            amount_to_bridge = (
                random_amount_to_use
                + config.DEFAULT_FEE_PER_PROJ * (1 + config.FEE_OFFSET)
            ) / eth_price_at_the_moment
            amount_to_buy = random_amount_to_use / eth_price_at_the_moment

            if project_name in config.ARBI_PROJECTS:
                w3 = self.w3_arbi
                params = config.PROJECTS[project_name]
            else:
                w3 = self.w3_nova
                params = config.PROJECTS[project_name]

            project_run_params = [w3, params, [amount_to_bridge, amount_to_buy]]
            to_run_params[project_name] = project_run_params
        return to_run_params
