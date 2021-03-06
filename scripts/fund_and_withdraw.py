from brownie import FundMe
from scripts.helper_functions import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"current entrance fee: {entrance_fee}")
    print("funding ...")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("withdrawing ...")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
