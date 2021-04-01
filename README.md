# blockchain_with_python

*The wallet.py file is located in the starter code folder, while the Jupyter Notebook used to write the code is contained in the wallet folder*

## A Quick Wallet Description ##

This code allows the user to send transactions in both test Bitcoin and Ethereum with the Python programming language. The private keys needed are read in via the getenv function to allow the private key to remain hidden. The rest of the code uses functions to bring in the necessary coin type, private key, account information, recipient address, and coin amount. 

## Getting Started ##

Before you get started, make sure you have the following dependencies installed:
- **import subprocess**
- **import os**
- **import json**
- **from dotenv import load_dotenv**
- **from web3 import Web3**
- **from bit import PrivateKeyTestnet**
- **from web3.middleware import geth_poa_middleware**
- **from eth_account import Account**
- **from bit.network import NetworkAPI**

## Installing HD-Wallet-Derive ##

In addition to the dependencies, you must have HD-Wallet-Derive installed. The derive library used is written in the PHP language, therefore you must have PHP set up on your machine. 
If you prefere a video walk through, start here: [HD-Wallet Install](https://youtu.be/IvcZZaIEL_4) 
Otherwise, please follow the steps below:
- Start by visiting the XAMPP website [here](https://www.apachefriends.org/index.html)
- On the green Download arrow, you should see an option to "click here for other versions". Click this link to install version 7.4.16
- When installing, keep the default component selections checked
- Once the XAMPP package is installed, navigate to the folder where the PHP binaries are located. This should be at C:\xampp\php
- dit the php.ini file (C:\xampp\php\php.ini) using Notepad and add the following line at the end of the file: extension=php_gmp.dll. This will enable a necessary PHP extension that hd-wallet-derive relies on.
- Next, you need to update the System Environment Variables and add the path containing the PHP binaries (C:\xampp\php) to the PATH environment variable.
- Use the Windows Command Prompt as Administrator by searching CMD and then choose the "Run as administrator" option.
- In the terminal screen, type the command below:
setx /M PATH "%PATH%;C:\xampp\php"
- If everthing was successful, you should see a confirmation message of, "SUCCESS: Specified value was saved."

## Test Transactions Created in This Activity ##

*The "send_tx" function was defined to be used for both the Ethereum and Test Bitcoin transactions. The code for this function is shown below:
def send_tx(coin, account, recipient, amount):
    if (coin == ETH):
        tx = create_tx(ETH,account,recipient,amount)
        signed_tx = account.sign_transaction(tx)
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(result.hex())
        return result.hex()
    elif (coin == BTCTEST):
        tx = create_tx(BTCTEST,account,recipient,amount)
        signed_tx = account.sign_transaction(tx)
        return NetworkAPI.broadcast_tx_testnet(signed_tx) *
        
The private key for each coin type was added to unique variable names for the account to be used in creating each transaction:
*btc_account = priv_key_to_account(BTCTEST, private_key_btc)*
*eth_account = priv_key_to_account(ETH, private_key)*
 
A test transaction was then sent with the required inputs:
 
**Bitcoin transaction**
send_tx(BTCTEST, btc_account, "mwqBUL2DpLM3SqWsNxanUwqv7jQxybN8mp", 0.00001)
The addressed used for this transaction was obtained using the Bip39 mnemonic code converter



 
