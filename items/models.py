from django.db import models
from units.models import Unit
from django.contrib.auth.models import User


# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(User, related_name="item",
                             on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, related_name="item",
                             on_delete=models.CASCADE)

    '''
        it is used to create foreign key between two models.
        Check unit model for more details.
    '''

    name = models.CharField(null=False, max_length=120)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "item"
        ordering = ["name"]  # this is used to add name in select box
