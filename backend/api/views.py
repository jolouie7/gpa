from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Account, Transaction, User
from .serializers import AccountSerializer, TransactionSerializer, UserSerializer

# Used for get and post requests
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Get all Transactions for a specific user
class TransactionList(APIView):
    def get(self, request):
        transactions = Transaction.objects.filter(user_id=request.user.id)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

# Build API to create Transactions that update the Current Balance of the Account
    def post(self, request):
        try:
          transaction = Transaction.objects.create(
              transaction_type=request.data['transaction_type'],
              note=request.data['note'],
              amount=request.data['amount'],
              account_id=request.data['account_id'],
              user_id=request.user.id
          )
          transaction.save()
        except:
          return Response({'message': 'Failed to create transaction'})

        try:
          account = Account.objects.get(id=request.data['account_id'])
          if request.data['transaction_type'] == 'DEBIT':
              account.current_balance -= request.data['amount']
          elif request.data['transaction_type'] == 'CREDIT':
              account.current_balance += request.data['amount']
          account.save()
        except:
          return Response({'message': 'Failed to update account balance'})

        return Response({'message': 'Transaction created successfully'})

# Build API to get all Accounts for a specific user
class AccountList(APIView):
    def get(self, request):
        accounts = Account.objects.filter(user_id=request.user.id)
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)