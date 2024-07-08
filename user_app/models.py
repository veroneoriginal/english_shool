from django.db import models
from django.contrib.auth.models import AbstractUser
from user_app.errors import CreateRoleExeption


class Role(models.Model):
    REGISTRATION = 'Зарегистрированный'
    STUDENT = 'Студент'
    TEACHER = 'Преподаватель'

    ROLE_CHOICES = [
        (REGISTRATION, 'Registered'),
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    ]
    name = models.CharField(max_length=50, unique=True, choices=ROLE_CHOICES, default=REGISTRATION)
    allow_roles = [REGISTRATION, STUDENT, TEACHER]

    def save(self, *args, **kwargs):
        if self.name not in self.allow_roles:
            raise CreateRoleExeption(f'Невозможно создать роль "{self.name}"')
        super(Role, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = models.CharField(unique=False, null=False, max_length=150)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    role = models.ManyToManyField(Role, related_name='users')
    password = models.CharField(unique=False, blank=True, null=False, max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        self.full_clean()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email
