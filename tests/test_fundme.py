from brownie.network import account
from brownie import network, accounts, exceptions
from scripts.helper_functions import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy
import pytest


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy()
    entrance_fee = fund_me.getEntranceFee() + 100
    print(entrance_fee)
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    # checking that we actually funded from our account
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    # checking that after we withdraw then there is no funds on our address anymore
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    fund_me = deploy()
    bad_actor = accounts.add()

    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
