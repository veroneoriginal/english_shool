from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ('registered', 'Registered'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]

    username = models.CharField(unique=False, null=False, max_length=150)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='registered')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
