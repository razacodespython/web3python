#!/usr/bin/python3
import os
from brownie import Token, accounts
from dotenv import load_dotenv

load_dotenv()

private_key = os.getenv("PRIVATE_KEY_1")
account = accounts.add(private_key)

def main():
    return Token.deploy("Rython2", "Ryt2", 18, 1e21, {'from': account})
