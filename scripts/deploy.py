from brownie import accounts, config, network, FundMe
from scripts.helper_functions import get_account, get_price_feed_address


def deploy():
    account = get_account()
    # pass the priceFeed address to the fundme contract
    price_feed_address = get_price_feed_address()
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(f"contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy()
