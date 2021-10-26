#!/usr/bin/python3
import os
os.system("brownie compile")
from dotenv import load_dotenv
from brownie import accounts, network, config
from brownie import SimpleCollectible
from .create_metadata import *


load_dotenv()
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache", "mainnet-fork"]
OPENSEA_URL = "https://ipfs.io/assets/{}/{}"


def deploy_and_create():
    account = get_account()
    sample_token_uri = NFT_main()
    print(sample_token_uri)
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    # print(
    #     f"Awesome, you can view your NFT at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}"
    # )
    # print("Please wait up to 20 minutes, and hit the refresh metadata button. ")
    return simple_collectible.address


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])

def main():
    a = deploy_and_create()
    print("abcdefghijklm:"+str(a)+":abcdefghijklm")

