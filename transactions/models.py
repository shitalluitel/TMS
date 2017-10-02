from django.db import models
from items.models import Item
from django.contrib.auth.models import User


# Create your models here.

class Transaction(models.Model):
    user = models.ForeignKey(User, related_name='transaction', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='transaction', on_delete=models.CASCADE)
    customer_name = models.CharField(null=False, max_length=120)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    created_date = models.DateField(auto_now_add=True)

