import unittest
from Bank import BankAccount

class TestBankAccount(unittest.TestCase):
    def test_initial_balance_default(self):
        acc = BankAccount(0)
        self.assertEqual(acc.get_balance(), 0)

    def test_initial_balance_positive(self):
        acc = BankAccount(100)
        self.assertEqual(acc.get_balance(), 100)

    def test_initial_balance_negative(self):
        with self.assertRaises(ValueError):
            BankAccount(-50)

    def test_deposit_positive(self):
        acc = BankAccount(0)
        acc.deposit(50)
        self.assertEqual(acc.get_balance(), 50)

    def test_deposit_zero(self):
        acc = BankAccount(0)
        with self.assertRaises(ValueError):
            acc.deposit(0)

    def test_deposit_negative(self):
        acc = BankAccount(0)
        with self.assertRaises(ValueError):
            acc.deposit(-10)

    def test_withdraw_positive(self):
        acc = BankAccount(100)
        acc.withdraw(50)
        self.assertEqual(acc.get_balance(), 50)

    def test_withdraw_zero(self):
        acc = BankAccount(100)
        with self.assertRaises(ValueError):
            acc.withdraw(0)

    def test_withdraw_negative(self):
        acc = BankAccount(100)
        with self.assertRaises(ValueError):
            acc.withdraw(-10)

    def test_withdraw_more_than_balance(self):
        acc = BankAccount(100)
        with self.assertRaises(ValueError):
            acc.withdraw(150)

    def test_multiple_operations(self):
        acc = BankAccount(100)
        acc.deposit(50)
        acc.withdraw(30)
        self.assertEqual(acc.get_balance(), 120)

    def test_get_balance(self):
        acc = BankAccount(200)
        self.assertEqual(acc.get_balance(), 200)

if __name__ == "__main__":
    unittest.main()
