from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from mixer.backend.django import mixer

from user_app.models import User, Role
from course_app.models import Course


class TestCoursesViewSet(APITestCase):
    """ Тесты для вьюшки CoursesViewSet """

    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            username='testuser',
            password='Testpassword123'
        )

        for _ in range(10):
            mixer.blend(Course)
        self.url = '/api/courses/'

    def test_unidentified_user_receives_all_courses(self):
        """ НЕаутентифицированный пользователь получает все курсы """

        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_courses(self):
        """ Аутентифицированный пользователь получает все курсы """

        # Аутентифицируем пользователя перед запросом
        self.client.force_authenticate(user=self.user)

        # Выполняем GET-запрос
        response = self.client.get(self.url, format='json')

        # Проверяем статус ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 10)

    def test_authenticated_user_can_create_a_new_course(self):
        """ Аутентифицированный пользователь c ролью "преподаватель" может создать новый курс """

        # Создаем роль "Преподаватель"
        teacher_role = Role.objects.create(name=Role.TEACHER)

        # Создаем пользователя с ролью "Преподаватель"
        # pylint: disable=W0612 unused-variable
        teacher, created = User.objects.get_or_create(email='teacher@example.com')
        teacher.set_password('teacherpassword')
        teacher.save()

        # Добавляем роль "Преподаватель" пользователю
        teacher.role.add(teacher_role)

        # Проверяем, добавлена ли роль "Преподаватель" пользователю
        self.assertIn(teacher_role, teacher.role.all())

        # Проверяем, что у пользователя есть роль "Преподаватель"
        self.assertTrue(teacher.role.filter(name=Role.TEACHER).exists())

        # Аутентифицируем пользователя и добавляем токен в заголовок
        self.client.force_authenticate(user=self.user)

        # Данные для создания нового курса
        data = {
            'name': 'New Course',
            'description': 'This is a new course description',
            'start_date': '2024-01-01',  # Дата начала курса
            'end_date': '2024-06-01',  # Дата окончания курса
        }

        # Отправляем POST запрос для создания курса
        response = self.client.post(self.url, data)

        # Проверяем, что курс был создан
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Убедимся, что курс был добавлен в базу
        self.assertEqual(Course.objects.count(), 11)

        # Проверим, что курс создан с правильными данными
        new_course = Course.objects.get(name='New Course')
        self.assertEqual(new_course.name, 'New Course')
        self.assertEqual(new_course.description, 'This is a new course description')
