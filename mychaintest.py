import unittest
from mychain import Transaction, Block
from mychain import hash_message


class TestHashing(unittest.TestCase):

    def test_hash(self):
        self.assertEqual(hash_message("Test"), hash_message("Test"))

    def test_hash_not_equeal(self):
        self.assertNotEquals(hash_message("Test"), hash_message("test"))


class TransactionTest(unittest.TestCase):

    def setUp(self):
        self.tx = Transaction("Satheesh", "Chaitra", 10)

    def test_new_transaction(self):
        self.assertEqual(self.tx.amount, 10)
        self.assertEqual(self.tx.sender, "Satheesh")
        self.assertEqual(self.tx.receiver, "Chaitra")


class BlockTest(unittest.TestCase):

    def setUp(self):
        self.tx = Transaction("Satheesh", "Chaitra", 10)
        self.block = Block()

    def test_add_block(self):
        self.assertEqual(self.block.transaction_count, 0)
        self.block.add_transaction(self.tx)
        self.assertEqual(self.block.transaction_count, 1)

    def test_not_final(self):
        self.assertIsNone(self.block.hash)

    def test_finalize(self):
        self.block.finalize()
        self.assertIsNotNone(self.block.hash)
        self.assertEqual(self.block.height, 1)


if __name__ == '__main__':
    unittest.main()
