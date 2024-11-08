from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class AdminUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Use Django's built-in password handling

