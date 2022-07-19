from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    fund_with_link,
    get_account,
    get_contract
)
from scripts.AdvancedCollectible.deploy import deploy_advanced_collectible
from brownie import network
import pytest
import time


def test_can_create_advanced_collectible_integration():
    # Arrange
    account = get_account()
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    advanced_collectible = deploy_advanced_collectible()
    fund_with_link(advanced_collectible)
    # Act
    creation_tx = advanced_collectible.createCollectible("None", {"from": account})
    requestId = creation_tx.events["RequestedCollectible"]["requestId"]
    time.sleep(200)
    # Assert
    assert advanced_collectible.tokenCounter() > 0