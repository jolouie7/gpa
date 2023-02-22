from django.urls import path
from .views import AccountDetailView, AccountListView, BalanceView, TransactionListView, UserList, TransactionCreateView, AccountCreateView

urlpatterns = [
    path('users/', UserList.as_view()),
    path('transactions/', TransactionListView.as_view(), name='transaction_list'),
    path('transactions/create/', TransactionCreateView.as_view(), name='transaction_create'),
    path('accounts/', AccountListView.as_view(), name='account_list'),
    path('accounts/<int:pk>', AccountDetailView.as_view(), name='account_detail'),
    path('accounts/create/', AccountCreateView.as_view(), name='account_create'),
    path('balance/<str:date>/', BalanceView.as_view())

]