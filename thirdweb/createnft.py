from thirdweb import ThirdwebSDK
from eth_account import Account
from dotenv import load_dotenv
from web3 import Web3
import os
from thirdweb.types.nft import NFTMetadataInput

# Load environment variables into this file
load_dotenv()

# This PRIVATE KEY is coming from your environment variables. Make sure to never put it in a tracked file or share it with anyone.
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")

# Add your own RPC URL here or use a public one
RPC_URL = "https://rinkeby.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161"

# Instantiate a new provider to pass into the SDK
provider = Web3(Web3.HTTPProvider(RPC_URL))

# Optionally, instantiate a new signer to pass into the SDK
signer = Account.from_key(PRIVATE_KEY)

# Finally, you can create a new instance of the SDK to use
sdk = ThirdwebSDK(provider, signer)

#sdk.deployer.deploy_nft_collection({'name':nft_name})
nft_col = sdk.get_nft_collection("0xcBF73C7bE3Ec116437fE72e8c3F48571Ab77aC51")
image = open('/Users/USER/Documents/0.png', "rb")

nft_col.mint(NFTMetadataInput.from_json({ 
     "name": "Cool NFT", 
    "description": "Minted with the Python SDK!", 
    "image": image
 }))