from web3 import Web3

#mainnet__url = "https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161"

#rpc urls are endpoints used to send and receive data to a specific blockchain
#here we're interacting with Polygon's testnet, the mumbai testnet
mumbai_rpc_url = "https://rpc-mumbai.maticvigil.com"

# The provider is your connection to a blockchain
web3 = Web3(Web3.HTTPProvider(mumbai_rpc_url))

#log if we're connected or not
print(web3.isConnected())

#get the blocknumber
print(web3.eth.blockNumber)

#get the balance
#balance is shown in Wei, which is a huge number. Wei is likes 'pennies' in the ethereum world
wallet_address = "0x55c9bBb71a5CC11c2f0c40362Bb691b33a78B764"
print(web3.eth.getBalance(wallet_address))

#balance here is formatted in ether, 
balance = web3.eth.getBalance(wallet_address)
print(web3.fromWei(balance,"ether"))