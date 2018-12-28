from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone

# Each account will have independent cateogries, and all transactions for a user will be limited by this
'''

CATEGORY

'''
class Category(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)  # The main category name
    group = models.CharField(max_length=200)        # For grouping categories together
    
    def __str__(self):
        return self.description

'''

ACCOUNT

'''
class Account(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
        
'''

TRANSACTION

'''
class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    sub_account = models.CharField(max_length=200, default='')  # Optional additional description, like when two CCs are part of the same account
    
    # "Original" from the raw data
    original_description = models.CharField(max_length=200, default='')
    original_category = models.CharField(max_length=200, default='')
    origina_transaction_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    
    # Description, category, and transaction date.  Wired up automatically on import, but user editable
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(default=timezone.now)
    
    # Actual ammount!
    ammount_cents = models.IntegerField()
    
    # TODO:  Methods to access ammounts in a sane (readable) way

    def __str__(self):
        return self.description + str(ammount)

