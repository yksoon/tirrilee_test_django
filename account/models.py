from django.db import models

# Create your models here.

class Member(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    phone = models.IntegerField()
    introduce = models.TextField()
    
    USERNAME_FIELD = "email"
    REQUIRES_FIELDS = ["nickname"]
    
    def __str__(self):
        return self.nickname