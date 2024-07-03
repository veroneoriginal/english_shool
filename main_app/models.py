from django.db import models


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
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
