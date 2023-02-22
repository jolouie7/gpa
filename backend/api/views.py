from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Account, Transaction, User
from .serializers import AccountSerializer, TransactionSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# Used for get and post requests
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Get all Transactions for a specific user
class TransactionListView(APIView):
    # authentication_classes = (TokenAuthentication)
    # permission_classes = (IsAuthenticated)
    print('----------in TransactionListView----------')
    authentication_classes = []
    permission_classes = []

    # def get(self, request):
    #     # print('------request----', request.user)
    #     transactions = Transaction.objects.filter(user_id=request.user.id)
    #     serializer = TransactionSerializer(transactions, many=True)
    #     return Response(serializer.data)

    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

# Build API to create Transactions that update the Current Balance of the Account
class TransactionCreateView(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.objects.all()

    def post(self, request):
        print('in TransactionCreateView')
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
class AccountListView(APIView):
    authentication_classes = []
    permission_classes = []
    # def get(self, request):
    #     accounts = Account.objects.filter(user_id=request.user.id)
    #     serializer = AccountSerializer(accounts, many=True)
    #     return Response(serializer.data)

    def get(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

class AccountCreateView(APIView):
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)