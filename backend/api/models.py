from django.db import models
import random

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Account(models.Model):
    account_number = models.CharField(max_length=16, unique=True, default=''.join([str(random.randint(0, 9)) for _ in range(16)]))
    current_balance = models.IntegerField(default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.account_number

class Transaction(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    transaction_type = models.CharField(choices=[('DEBIT', 'Debit'), ('CREDIT', 'Credit')], max_length=6)
    note = models.CharField(max_length=200)
    amount = models.IntegerField()
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)