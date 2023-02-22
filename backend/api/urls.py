from django.urls import path
from .views import AccountListView, TransactionListView, UserList, TransactionCreateView, AccountCreateView

urlpatterns = [
    path('users/', UserList.as_view()),
    path('transactions/', TransactionListView.as_view(), name='transaction_list'),
    path('transactions/create/', TransactionCreateView.as_view(), name='transaction_create'),
    path('accounts/', AccountListView.as_view(), name='account_list'),
    path('accounts/create/', AccountCreateView.as_view(), name='account_create'),
]