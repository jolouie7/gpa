from django.test import TestCase
from api.models import User, Account, Transaction

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='testuser@example.com', password='password')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')

class AccountTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='testuser@example.com', password='password')
        self.account = Account.objects.create(account_number='1234567890123456', current_balance=0, user_id=self.user)

    def test_account_str(self):
        self.assertEqual(str(self.account), '1234567890123456')

    def test_account_balance(self):
        self.assertEqual(self.account.current_balance, 0)

class TransactionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='testuser@example.com', password='password')
        self.account = Account.objects.create(account_number='1234567890123456', current_balance=200, user_id=self.user)
        self.credit_transaction = Transaction.objects.create(transaction_type='CREDIT', note='Test debit', amount=100, account_id=self.account, user_id=self.user)
        self.debit_transaction = Transaction.objects.create(transaction_type='DEBIT', note='Test debit', amount=100, account_id=self.account, user_id=self.user)

    def test_credit_transaction(self):
        self.assertEqual(self.credit_transaction.transaction_type, 'CREDIT')
        self.account.current_balance += self.credit_transaction.amount
        self.account.save()
        self.assertEqual(self.account.current_balance, 300)

    def test_debit_transaction(self):
        self.assertEqual(self.debit_transaction.transaction_type, 'DEBIT')
        self.account.current_balance -= self.debit_transaction.amount
        self.account.save()
        self.assertEqual(self.account.current_balance, 100)