// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
// import "@openzeppelin/contracts/utils/Counters.sol";

contract SimpleCollectible is ERC721 {
    // using Counters for Counters.Counter;
    // Counters.Counter private tokenCounter;
    uint256 public tokenCounter;

    constructor() ERC721("Dogie", "Dog") public {
        tokenCounter = 0;
    }

    function createCollectible(string memory tokenURI) public returns(uint256){
        // uint256 newTokenId = tokenCounter.current();
        uint newTokenId = tokenCounter;
        _safeMint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
        tokenCounter = tokenCounter + 1;
        // tokenCounter.increment();
        return newTokenId;
    }
}
