from thirdweb import ThirdwebSDK
import pandas as pd
import os
from dotenv import load_dotenv

#Load the environment variables
load_dotenv()
#Load the private keys
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
#The column with wallets from our dataset
col_list = ['wallet']
#Read our dataset with our wallet selection
data = pd.read_csv('wallet.csv',usecols=col_list)
#Instantiate and connect it to the thirdweb SDK
sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, "mumbai")
#Connect our smart contract to our program
token = sdk.get_token("0xB91fc509Fe99AeEef70D6d7Ce234039F2e97F48a")
#Create an array/list from our data
wallets = data['wallet']
#Define length for the for loop
n_wallets = len(wallets)
#Mint and transfer to the wallet
for i in range(n_wallets):
    print("start minting for" + wallets[i])
    minting = token.mint_to(wallets[i],1000)
    print("done minting for " + wallets[i] + "\n"+"Receipt: " + minting.transactionHash.hex())


