from django.urls import path
from .views import account_list_view, account_detail_view, balance_view, transaction_detail_view, user_list, transaction_create_view, account_create_view

urlpatterns = [
    path('users/', user_list, name='user_list'),
    path('transactions/<int:user_id>/', transaction_detail_view, name='transaction_list_detail_view'),
    path('transactions/create/', transaction_create_view, name='transaction_create_view'),
    path('accounts/', account_list_view, name='account_list_view'),
    path('accounts/<int:user_id>/', account_detail_view, name='account_detail_view'),
    path('accounts/create/', account_create_view, name='account_create_view'),
    path('balance/<int:user_id>/<str:date>/', balance_view, name='balance_view'),
]