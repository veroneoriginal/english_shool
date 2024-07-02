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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        self.full_clean()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    # students = models.ManyToManyField(User, related_name='enrolled_courses', blank=True)
    # related_name - имя обратного отношения, которое позволяет доступ к курсам через модель пользователя.
    # User.enrolled_courses вернет все курсы, на которые зарегистрирован студент.
    # blank=True: Поле может быть пустым; это означает, что курс может не иметь зарегистрированных студентов.

    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
