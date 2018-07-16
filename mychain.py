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
        self.payload_hash = self._hash_payload()
        self.transaction_count = 0

    def _hash_payload(self):
        return self._hash_transactions()

    def _hash_transactions(self):
        curr_hash = ""
        for tx in self.transactions:
            txn_rep = curr_hash.join(jsonpickle.encode(tx))
            curr_hash = hash_message(txn_rep)
        return curr_hash

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.transaction_count = len(self.transactions)

    def _hash_block(self):
        self.payload_hash = self._hash_payload()
        blockheader_data = {
            'payload_hash': self.payload_hash,
            'timestamp': self.timestamp,
            'prev_hash': self.prev_hash,
            'total_transactions': self.transaction_count
        }
        block_rep = jsonpickle.encode(blockheader_data)
        return hash_message(block_rep)

    def finalize(self):
        if self.hash is None:
            self.hash = self._hash_block()
        else:
            raise ValueError("Block already final")

    def validate(self):
        return self.hash == self._hash_block()


def hash_message(data):
    return hashlib.sha256(data).hexdigest()


def savechain(blockchain, datafile):
    with open(datafile, "wb") as bf:
        bf.write(jsonpickle.encode(blockchain))


def loadchain(datafile):
    with open(datafile) as bf:
        return jsonpickle.loads(bf.read())


def validatechain(blockchain):
    print(len(blockchain))
    for block in blockchain:
        if block.validate():
            print("Block #{} is valid".format(block.height))
            if block.height != 1:
                if block.prev_hash != blockchain[block.height-2].hash:
                    print("Prev hash {} != Prev block hash {}".format(block.prev_hash,
                                                                      blockchain[block.height-2].hash))
                    return False
                print("Block #{} Prev hash {} == Prev block hash {}".format(block.height, block.prev_hash,
                                                                            blockchain[block.height-2].hash))
        else:
            print ("Block {} is invalid".format(block.height))
            return False
    else:
        return True


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
