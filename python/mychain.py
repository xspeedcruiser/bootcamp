# -*- coding: utf-8 -*-
import datetime
import hashlib
from time import time
import jsonpickle


class Transaction:
    """
    Transaction stores the following information
    1. Sender
    2. Receiver
    3. Amount
    4. Timestamp

    TODO: Add a generated transaction ID based on some hashing technique 
    """

    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time()

    def __repr__(self):
        return 'Transaction : {} sent {} units to {}'.format(
            self.sender, self.amount, self.receiver
        )


class Block:
    def __init__(self, blockchain=None):
        self.transactions = []
        self.prev_hash = None
        self.height = None
        if blockchain is not None:
            self.prev_hash = blockchain[-1].hash
            self.height = len(blockchain) + 1
        else:
            self.height = 1
        self.hash = None
        self.timestamp = time()
        self.transaction_count = 0

    def _hash_payload(self):
        return self._hash_transactions()
    
    
    def _hash_transactions(self):
        """
        This is a very crude implementation of transactions hashing where
        
        hash = hash(curr_hash + curr_txn)
        
        We will switch this to a merkle-tree implementaion in the future 
        workshops. A merkle-tree is a data-structure to store the transaction 
        in a form where we can validate a transaction in an efficient manner.
        """
        curr_hash = ""
        #TODO
        return curr_hash

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.transaction_count = len(self.transactions)

    def _hash_block(self):
        #TODO implement the hashblock
        """
        1. Get transaction hash -> PAYLOADHASH
        2. Form block header data structure
        3. Calculate the hash of
        blockhash = hash( blockheader)
        """
        self.payload_hash = self._hash_payload()
        blockheader_data = {
            'payload_hash': "",
            'timestamp': "",
            'prev_hash': "",
            'total_transactions': ""
        }
        block_rep = ""
        return hash_message(block_rep)

    def finalize(self):
        if self.hash is None:
            self.hash = self._hash_block()
        else:
            raise ValueError("Block already final")

    def validate(self):
        return false


def hash_message(data):
    #TODO  use SHA256 and return HEX digest
    return "HASH"


def savechain(blockchain, datafile):
    with open(datafile, "wb") as bf:
        bf.write(jsonpickle.encode(blockchain))


def loadchain(datafile):
    with open(datafile) as bf:
        return jsonpickle.loads(bf.read())


def validatechain(blockchain):
    return False


def main():
    jsonpickle.set_encoder_options("json", sort_keys=True, indent=4)
    blockchain = []
    #block = load("blockchain.json")

    block = Block()
    a = Transaction("Satheesh", "Chaitra", 10)
    b = Transaction("Chaitra", "Nala", 5)
    # print(a)
    block.add_transaction(a)
    block.add_transaction(b)
    block.finalize()
    print(block.validate())
    #c = Transaction("Nala", "Simba", 1)
    # block.add_transaction(c)
    blockchain.append(block)
    newblock = Block(blockchain)
    a = Transaction("Vintoh", "Jeeva", 10)
    newblock.add_transaction(a)
    newblock.finalize()
    blockchain.append(newblock)
    savechain(blockchain, "blockchain.json")
    # validatechain(blockchain)
    blockchain = loadchain("blockchain.json")
    thirdblock = Block(blockchain)
    d = Transaction("Jeeva", "Satheesh", 2)
    thirdblock.add_transaction(d)
    thirdblock.finalize()
    blockchain.append(thirdblock)
    savechain(blockchain, "blockchain.json")
    print(validatechain(blockchain))


if __name__ == "__main__":
    main()
