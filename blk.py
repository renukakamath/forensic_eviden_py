
import json
from web3 import Web3, HTTPProvider


# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:9545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]
compiled_contract_path = 'C:/Users/renuk/OneDrive/Desktop/RISS/blockchain/forensic_eviden (2)/forensic_eviden (2)/forensic_eviden/forensic_eviden/node_modules/.bin/build/contracts/forensic.json'
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0xfeD24Fb1b0E1691C3a455F2231e4389A70117CA8'
syspath=r"C:\\Users\\renuk\\OneDrive\\Desktop\\RISS\\blockchain\\forensic_eviden (2)\\forensic_eviden (2)\\forensic_eviden\\forensic_eviden\static\\"
