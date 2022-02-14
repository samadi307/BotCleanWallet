from web3 import Web3
import json
import config
import time

#################################################
bsc = "https://data-seed-prebsc-1-s1.binance.org:8545/"
idchain = 97 #ID chain ##97 for teste chain ##56 for mainet chain
sender_address = '####'   #send from this address
privatekey = "####" #Private key of account "sender_address"
tothisadresse= "####"     #to this address
contract_address = '####' #adresse BSC majuscule "USDT","BCOIN".... 
#abi tahowa khassek tbedlo tatjebdo men contract
abi = json.loads('####')
#print(web3.isConnected())
#################################################
def checkbnb():
    web3 = Web3(Web3.HTTPProvider(bsc))
	# print(web3.isConnected())
    balance = web3.eth.get_balance(sender_address)
	# print(balance)
    humanReadable = web3.fromWei(balance,'ether')
	# print(humanReadable)
    return(humanReadable)
#checkbnb()

while(True):
    print("BNB: " + str(checkbnb()))
    web3 = Web3(Web3.HTTPProvider(bsc))
    contract = web3.eth.contract(address=contract_address, abi=abi)
    totalSupply = contract.functions.totalSupply().call()
    ##print(web3.fromWei(totalSupply, 'ether'))
    ##print(contract.functions.name().call())
    print('symbole: ' + str(contract.functions.symbol().call()))
    balanceOf = contract.functions.balanceOf(sender_address).call()
    print('balance of '+ str(contract.functions.symbol().call()) + ' is : ' + str(web3.fromWei(balanceOf, 'ether')))
    if (web3.fromWei(balanceOf, 'ether') > 1 and checkbnb() > 0):
        send =  web3.fromWei(balanceOf, 'ether')
        amount = web3.toWei(send, 'ether')
        #print(amount)
        nonce = web3.eth.getTransactionCount(sender_address)
        #print(nonce)
        token_tx = contract.functions.transfer(tothisadresse, amount).buildTransaction({
            'chainId':idchain, 'gas': 100000,'gasPrice': web3.toWei('10','gwei'), 'nonce':nonce
        })
        sign_txn = web3.eth.account.signTransaction(token_tx, private_key=privatekey)
        web3.eth.sendRawTransaction(sign_txn.rawTransaction)
        print(f"Transaction has been sent to {tothisadresse}")
        time.sleep(5)
    else:
        print(str(contract.functions.symbol().call()) + " not Found")
