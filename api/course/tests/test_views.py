from pprint import pprint

from rest_framework import status
from rest_framework.test import APITestCase
from mixer.backend.django import mixer

from course_app.models import Course
from user_app.models import User


class TestCoursesViewSet(APITestCase):
    """ Тесты для вьюшки CoursesViewSet """

    def setUp(self):
        self.user = mixer.blend(User, email='test@test.ru')
        self.user.set_password('111')
        self.user.save()

        for _ in range(10):
            mixer.blend(Course)
        self.url = '/api/courses/'

    def test_do_not_get_all_courses(self):
        """ НЕаутентифицированный пользователь НЕ получает все курсы """

        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_all_courses(self):
        """ Аутентифицированный пользователь получает все курсы """

        # Аутентифицируем пользователя перед запросом
        self.client.force_authenticate(user=self.user)

        # Выполняем GET-запрос
        response = self.client.get(self.url, format='json')

        pprint(response.json())

        # # Проверяем статус ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 10)
