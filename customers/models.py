from django.db import models
from users.models import User


# Create your models here.

class Customer(models.Model):
    user = models.ForeignKey(User, related_name='Customer', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=244)
    phone_number = models.CharField(max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "customer"
        ordering = ["name"]  # this is used to add name in select box
