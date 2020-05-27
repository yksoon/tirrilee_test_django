from django.db import models
from django.conf import settings

# Create your models here.

class Board(models.Model):
    product = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=10)
    picture = models.ImageField(upload_to="")
    
    def __str__(self):
        return self.product