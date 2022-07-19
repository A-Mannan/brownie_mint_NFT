from brownie import AdvancedCollectible, accounts, config
from scripts.helpful_scripts import get_account, get_breed, fund_with_link
import time

def create_collectible():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible.address)
    tx = advanced_collectible.createCollectible("None", {"from": account})
    tx.wait(1)
    time.sleep(200)
    requestId = tx.events["RequestedCollectible"]["requestId"]
    tokenId = advanced_collectible.requestIdToTokenId(requestId)
    breed = get_breed(advanced_collectible.tokenIdToBreed(tokenId))
    print(f"Dog breed of w.r.t to tokenId {tokenId} is {breed}")

def main():
    create_collectible()