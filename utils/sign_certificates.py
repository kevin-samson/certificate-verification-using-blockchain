from web3 import Web3
from eth_account.messages import encode_defunct


class SecureDocumentVerifier:
    def __init__(self,url,address,private_key):
        self.url = url
        self.address = address
        self.private_key = private_key
        self.w3 = Web3(Web3.HTTPProvider(url))
        self.account = self.w3.eth.account.from_key(private_key)
        print(self.w3.is_connected() and "Connected to the blockchain" or "Failed to connect to the blockchain")

    def sign_message(self,data):
        message = encode_defunct(data)
        signed_message = self.w3.eth.account.sign_message(message,self.private_key)
        return signed_message.messageHash.hex(),signed_message.signature.hex()
    
    def deploy_contract(self,bytecode,abi):
        contract = self.w3.eth.contract(abi=abi, bytecode=bytecode)
        transaction = contract.constructor().build_transaction({
            'from': self.address,
            'nonce': self.w3.eth.get_transaction_count(self.address),
            'gas': 1728712,
            'gasPrice': self.w3.eth.gas_price,
        })
        signed = self.w3.eth.account.sign_transaction(transaction, private_key=self.private_key)
        transaction_hash = self.w3.eth.send_raw_transaction(signed.rawTransaction)
        transaction_receipt = self.w3.eth.wait_for_transaction_receipt(transaction_hash)
        return transaction_receipt
    
    def add_document(self,document_hash,document_sign,contract_address,abi):
        contract = self.w3.eth.contract(address=contract_address, abi=abi)
        transaction = contract.functions.addDocument(document_hash,document_sign).build_transaction({
            'from': self.address,
            'nonce': self.w3.eth.get_transaction_count(self.address),
            'gas': 1728712,
            'gasPrice': self.w3.eth.gas_price,
        })
        signed = self.w3.eth.account.sign_transaction(transaction, private_key=self.private_key)
        transaction_hash = self.w3.eth.send_raw_transaction(signed.rawTransaction)
        transaction_receipt = self.w3.eth.wait_for_transaction_receipt(transaction_hash)
        return transaction_receipt
    
    def verify_document(self,document_hash,contract_address,abi):
        contract = self.w3.eth.contract(address=contract_address, abi=abi)
        return contract.functions.documentExists(document_hash).call()
    
    def changeDocumentStatus(self,document_hash,status,contract_address,abi):
        contract = self.w3.eth.contract(address=contract_address, abi=abi)
        transaction = contract.functions.changeDocumentStatus(document_hash,status).build_transaction({
            'from': self.address,
            'nonce': self.w3.eth.get_transaction_count(self.address),
            'gas': 1728712,
            'gasPrice': self.w3.eth.gas_price,
        })
        signed = self.w3.eth.account.sign_transaction(transaction, private_key=self.private_key)
        transaction_hash = self.w3.eth.send_raw_transaction(signed.rawTransaction)
        transaction_receipt = self.w3.eth.wait_for_transaction_receipt(transaction_hash)
        return transaction_receipt

    def getDocumentStatus(self,document_hash,contract_address,abi):
        contract = self.w3.eth.contract(address=contract_address, abi=abi)
        return contract.functions.getDocumentStatus(document_hash).call()