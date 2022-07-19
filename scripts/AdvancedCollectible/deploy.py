from brownie import AdvancedCollectible, config, network
from scripts.helpful_scripts import (
    get_account,
    get_contract,
    get_publish_source
)


def deploy_advanced_collectible():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
        publish_source=get_publish_source(),
    )
    print("Deployed!")
    return advanced_collectible


def main():
    deploy_advanced_collectible()
