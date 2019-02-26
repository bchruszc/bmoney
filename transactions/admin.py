from django.contrib import admin
from models import Category, Account, Transaction, OFXFileTask

# Register your models here.
admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(OFXFileTask)
