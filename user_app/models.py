from django.core.validators import EmailValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # класс от которого наследуемся имеет username, first_name, last_name, email, password

    username = models.CharField(unique=False, null=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
