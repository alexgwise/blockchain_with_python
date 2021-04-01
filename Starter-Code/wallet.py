# Import dependencies
import subprocess
import os
import json
from dotenv import load_dotenv
from web3 import Web3
from bit import PrivateKeyTestnet
from web3.middleware import geth_poa_middleware
from eth_account import Account
from bit.network import NetworkAPI

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

# Import constants.py and necessary functions from bit and web3
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
from constants import *

w3.eth.blockNumber

#private_key = "167dd9832564b4cd53d6c92d729f6fd1dbe9852dd331c28a3dcc8e94ad407724"
private_key = os.getenv("PRIVATE_KEY")
len(private_key)

private_key_btc = os.getenv("PRIVATE_KEY_BTC")
len(private_key_btc)

# ended up just reading in private keys from .env file due to error message that couldn't be resolved in office hours

# Create a function called `derive_wallets`
#def derive_wallets(coin_type, mnemonic):
    #command = 'php C:/Users/alexg/FinTech_edit_files/smu-dal-fin-pt-10-2020-u-c/02-Homework/19-Blockchain-Python/blockchain_with_python/wallet/derive/hd-wallet-derive.php -g --mnemonic="{mnemonic}" --cols=privkey --format=json --coin={coin_type} --numderive=1'
   #p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
   # output, err = p.communicate()
   # p_status = p.wait()
   # return json.loads(output)

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    if (coin == ETH):
        return Account.privateKeyToAccount(priv_key)
    elif (coin == BTCTEST):
        return PrivateKeyTestnet(priv_key)

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, recipient, amount):
    if (coin == ETH):
        gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )
        return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
    }
    elif (coin == BTCTEST):
        return PrivateKeyTestnet.prepare_transaction(account.address, [(recipient, amount, "btc")])
    
# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
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
        return NetworkAPI.broadcast_tx_testnet(signed_tx)

btc_account = priv_key_to_account(BTCTEST, private_key_btc)

eth_account = priv_key_to_account(ETH, private_key)

send_tx(BTCTEST, btc_account, "mwqBUL2DpLM3SqWsNxanUwqv7jQxybN8mp", 0.00001)

send_tx(ETH, eth_account, "0x9c87c013941904Db6ec3af17cfe16dBe4d8fEeFc", 1)