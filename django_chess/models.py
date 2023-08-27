from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=15, name="username", unique=True)
    password = models.CharField(max_length=100, name="password")

    def __str__(self):
        return f"User: {self.username}"
