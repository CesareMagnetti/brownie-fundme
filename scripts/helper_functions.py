from brownie import accounts, network, config, MockV3Aggregator

FORKED_LOCAL_ENVIRONMENTS = ["mainet-fork", "mainet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
DECIMALS = 8  # because we already do conversion in get_price
STARTING_PRICE = 200000000000  # eth


def get_price_feed_address():
    print("the active network is:", network.show_active())
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        # deploy a mock interface (in contracts/test)
        if len(MockV3Aggregator) <= 0:
            print(
                "deploying mock aggregator interface (see contracts/test/MockV#Aggregator.sol ..."
            )
            MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
            print("Mock deployed.")
        price_feed_address = MockV3Aggregator[-1].address
    else:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    return price_feed_address


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        account = accounts[0]
    else:
        account = accounts.add(config["wallets"]["from_key"])
    return account
