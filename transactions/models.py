from django.db import models
from items.models import Item
from users.models import User
from customers.models import Customer


# Create your models here.

class Transaction(models.Model):
    user = models.ForeignKey(User, related_name='transaction', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='transaction')
    customer = models.ForeignKey(Customer, related_name='transaction')
    # customer_name = models.CharField(null=False, max_length=120)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    created_date = models.DateField(auto_now_add=True)
    valid_date = models.DateTimeField(auto_now_add=True)
