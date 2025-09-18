import unittest
from unittest.mock import Mock
from Bank import BankAccount

class NotificationSystem:
    def notify(self, message):
        pass

class BankAccountWithNotification(BankAccount):
    def __init__(self, initial_balance=0, notifier=None):
        super().__init__(initial_balance)
        self.notifier = notifier

    def deposit(self, amount):
        super().deposit(amount)
        if self.notifier:
            self.notifier.notify(f"Deposit of {amount} successful. New balance: {self.get_balance()}")

class TestBankAccountDepositIntegration(unittest.TestCase):
    def test_deposit_triggers_notification(self):
        mock_notifier = Mock(spec=NotificationSystem)
        acc = BankAccountWithNotification(100, notifier=mock_notifier)
        acc.deposit(50)
        mock_notifier.notify.assert_called_once_with("Deposit of 50 successful. New balance: 150")

    def test_deposit_no_notifier(self):
        acc = BankAccountWithNotification(100)
        acc.deposit(50)
        self.assertEqual(acc.get_balance(), 150)

    def test_deposit_invalid_amount_negative(self):
        mock_notifier = Mock(spec=NotificationSystem)
        acc = BankAccountWithNotification(100, notifier=mock_notifier)
        with self.assertRaises(ValueError):
            acc.deposit(-10)
        mock_notifier.notify.assert_not_called()

    def test_deposit_invalid_amount_zero(self):
        mock_notifier = Mock(spec=NotificationSystem)
        acc = BankAccountWithNotification(100, notifier=mock_notifier)
        with self.assertRaises(ValueError):
            acc.deposit(0)
        mock_notifier.notify.assert_not_called()

    def test_multiple_deposits_notifications(self):
        mock_notifier = Mock(spec=NotificationSystem)
        acc = BankAccountWithNotification(100, notifier=mock_notifier)
        acc.deposit(50)
        acc.deposit(25)
        self.assertEqual(mock_notifier.notify.call_count, 2)
        mock_notifier.notify.assert_any_call("Deposit of 50 successful. New balance: 150")
        mock_notifier.notify.assert_any_call("Deposit of 25 successful. New balance: 175")

    def test_large_deposit_notification(self):
        mock_notifier = Mock(spec=NotificationSystem)
        acc = BankAccountWithNotification(100, notifier=mock_notifier)
        large_amount = 10**6
        acc.deposit(large_amount)
        mock_notifier.notify.assert_called_once_with(f"Deposit of {large_amount} successful. New balance: {100 + large_amount}")

    def test_notification_failure_handling(self):
        mock_notifier = Mock(spec=NotificationSystem)
        mock_notifier.notify.side_effect = Exception("Notification failed")
        acc = BankAccountWithNotification(100, notifier=mock_notifier)
        # Deposit should still succeed, but notification raises
        with self.assertRaises(Exception):
            acc.deposit(50)
        self.assertEqual(acc.get_balance(), 150)

    def test_deposit_after_withdrawal_notification(self):
        mock_notifier = Mock(spec=NotificationSystem)
        acc = BankAccountWithNotification(200, notifier=mock_notifier)
        acc.withdraw(50)
        acc.deposit(30)
        mock_notifier.notify.assert_called_once_with("Deposit of 30 successful. New balance: 180")

    def test_notifier_replacement(self):
        mock_notifier1 = Mock(spec=NotificationSystem)
        mock_notifier2 = Mock(spec=NotificationSystem)
        acc = BankAccountWithNotification(100, notifier=mock_notifier1)
        acc.deposit(20)
        acc.notifier = mock_notifier2
        acc.deposit(30)
        mock_notifier1.notify.assert_called_once_with("Deposit of 20 successful. New balance: 120")
        mock_notifier2.notify.assert_called_once_with("Deposit of 30 successful. New balance: 150")

if __name__ == "__main__":
    unittest.main()
