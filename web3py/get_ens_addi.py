from web3 import Web3
from ens import ENS

#mainnet__url = "https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161"

rpc_url = "https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161"

# The provider is your connection to a blockchain
web3 = Web3(Web3.HTTPProvider(rpc_url))

#log if we're connected or not
print(web3.isConnected())

ns = ENS.fromWeb3(web3)

print(ns.address(input("enter your ens domain to get your wallet address\n")))
