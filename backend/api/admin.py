from django.contrib import admin
from .models import Account, Transaction, User

admin.site.register(Transaction)
admin.site.register(Account)