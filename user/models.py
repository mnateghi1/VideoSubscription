from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.TextField(null=True)
    phone_number = models.CharField(max_length=12, null=True)

    def __str__(self):
        return self.username

