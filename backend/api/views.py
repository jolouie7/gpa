from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Account, Transaction, User
from .serializers import AccountSerializer, TransactionSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


# Get all users
# Create a new user
# !OVERRIDE DEFAULT USER MODEL WITH CUSTOM USER MODEL
@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get all Transactions for a specific user
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def transaction_detail_view(request, user_id):
    try:
        transactions = Transaction.objects.filter(user_id=user_id)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
    except Account.DoesNotExist:
        return Response({'message': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def transaction_create_view(request):
    serializer = TransactionSerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
    except:
        return Response({'message': 'Failed to create transaction'})

    # Could also make a separate function to update account balance
    try:
        account_number = serializer.validated_data['account_id']
        account = Account.objects.get(account_number=account_number)
        transaction_type = serializer.validated_data['transaction_type']
        amount = serializer.validated_data['amount']

        if transaction_type == 'DEBIT':
            account.current_balance -= amount
        elif transaction_type == 'CREDIT':
            account.current_balance += amount

        account.save()

        return Response({'message': 'Transaction created successfully'}, status=status.HTTP_201_CREATED)
    except:
        return Response({'message': 'Failed to update account balance'})

# Get all accounts
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def account_list_view(request):
    try:
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)
    except Account.DoesNotExist:
        return Response({'message': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def account_detail_view(request, user_id):
    try:
        account = Account.objects.filter(user_id=user_id)
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)
    except Account.DoesNotExist:
        return Response({'message': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def account_create_view(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Build API to get Balance for a certain date
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def balance_view(request, date, user_id):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return Response({'error': 'Invalid date format. Please use YYYY-MM-DD'}, status=400)

    transactions = Transaction.objects.filter(user_id=user_id, date_created__lte=date_obj)
    balance = 0
    for transaction in transactions:
        print("transaction: ", transaction.transaction_type)
        if transaction.transaction_type == 'DEBIT':
            balance -= transaction.amount
        elif transaction.transaction_type == 'CREDIT':
            balance += transaction.amount
    return Response({'balance': balance})

# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Please provide both username and password'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'error': 'Invalid Credentials'},
#                         status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key},
#                     status=HTTP_200_OK)

# @csrf_exempt
# @api_view(["GET"])
# def sample_api(request):
#     data = {'sample_data': 123}
#     return Response(data, status=HTTP_200_OK)