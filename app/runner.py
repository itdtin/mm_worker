import random
import time
from pathlib import Path
import os

from queue import Queue
from web3 import Account, Web3
from logzero import logger

import config
import flows_config
from app.scripts import scripts


class Runner:

    def __init__(self, wallets_path):
        self.wallets = self.import_wallets(wallets_path)
        self.scripts = {func.__name__: func for func in scripts()}
        self.wallets_queue = Queue()
        for wallet in self.wallets:
            self.wallets_queue.put(wallet)

        self.wait_wlt = (config.WAIT_BTW_WALLET_MIN, config.WAIT_BTW_WALLET_MAX)
        self.wait_projects = (config.WAIT_BTW_PROJECT_MIN, config.WAIT_BTW_PROJECT_MAX)

    def do_work(self):
        print("do work")
        results = {}

        while self.wallets_queue.qsize():
            wallet = self.wallets_queue.get()
            results[wallet.address] = {}
            self.run_projects_in_order(wallet)
            self.make_pause_btw_wlt()

    def run_projects_in_order(self, wallet):
        for project_name, project_params in flows_config.PROJECTS.items():
            self.run_project(wallet, project_name, project_params)
            self.make_pause_btw_projects()

    def run_project(self, wallet, project_name: str, run_args=None):
        logger.info(f"Starting {project_name}")
        if not run_args:
            run_args = {}  
        args = [wallet] + [run_args]
        flow_ = self.scripts.get(run_args["script"])
        if flow_:
            result = flow_(*args)
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
