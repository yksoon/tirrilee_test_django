from django.db import models
from django.conf import settings
from django.utils import timezone

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.



class Board(models.Model):
    product = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=10)
    #picture = models.ImageField(upload_to="")
    nickname = models.CharField(max_length=50, null=False)
    image = ProcessedImageField(
        upload_to="board/images",
        processors=[ResizeToFill(700,400)],
        format='jpeg',
        options={'quality': 90}
    )
    
    def __str__(self):
        return self.product