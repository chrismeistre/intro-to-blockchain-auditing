// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

import "OpenZeppelin/openzeppelin-contracts@4.4.0/contracts/token/ERC20/ERC20.sol";

contract HackSouthToken is ERC20 {

    mapping(address => uint256) public balances;
    address public owner;
    uint256 amount;

    constructor(string memory name_, string memory symbol_, address owner_, uint256 amount_) ERC20(name_, symbol_){
        _mint(owner_, amount_);
        owner = owner_;
        balances[owner] = amount_;
    }

    function setOwner() public onlyOwner{
        // set new owner of contract
        owner = msg.sender;
    }

    function balanceOf(address who) public view override returns (uint256 amount) {
        // return balance of user
        address sender = msg.sender;
        return balances[sender];
    }

    function adjustBalance(address who, uint256 amount) public {
        balances[who] += amount;
    }

    modifier onlyOwner {
        require(owner == msg.sender, "Ownership Assertion: Caller is not the owner.");
        _;
    }

}
