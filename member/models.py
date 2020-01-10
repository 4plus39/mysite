from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
