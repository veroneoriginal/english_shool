from django.db import models


class Teachers(models.Model):
    """Модель преподавателя"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'


class Students(models.Model):
    """Модель студента"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'


class Course(models.Model):
    """Модель курса"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'


class Schedule(models.Model):
    """Модель расписания"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'
