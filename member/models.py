from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField('更新時間', auto_now=True)

    def __str__(self):
        return self.name
