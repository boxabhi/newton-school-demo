from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=12)
    is_phone_no_verified = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

