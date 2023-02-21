from rest_framework import serializers
from .models import Account, Transaction, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'date_created')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'account_number', 'user_id', 'current_balance')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'date_created', 'date_updated', 'transaction_type', 'note', 'amount', 'account_id', 'user_id')