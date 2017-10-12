from django.db import models
from users.models import User


# Create your models here.

class Unit(models.Model):
    user = models.ForeignKey(User, related_name='Unit', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    print_name = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # this is necessary to create select box

    def __str__(self):
        return self.print_name

    class Meta:
        db_table = "unit"
        ordering = ["print_name"]  # this is used to add name in select box
