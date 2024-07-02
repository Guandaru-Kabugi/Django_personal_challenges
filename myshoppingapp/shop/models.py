from django.db import models

# Create your models here.

class Item(models.Model):
    def __str__(self) -> str:
        return self.item_name
    item_name = models.CharField(max_length=150)
    item_descp = models.CharField(max_length=150)
    item_price = models.IntegerField()