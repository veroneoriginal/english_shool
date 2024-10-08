from rest_framework import status
from rest_framework.test import APITestCase

from user_app.models import (
    User,
    Role,
)


class TestUserRegistrationView(APITestCase):
    """
    Тесты для вьюшки UserRegistrationView
    (регистрация пользователя)
    """

    def setUp(self):
        self.url = '/api/registration/'

    def test_user_registration_ok(self):
        """ Успешная регистрация """

        request_data = {
            "email": "test_1@example.ru",
            "password": "222222",
        }
        response = self.client.post(self.url, data=request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        User.objects.get(email=request_data['email'], role__name=Role.REGISTRATION)

    def test_validation_error(self):
        """ Плохой email """

        request_data = {
            'email': 'test',
            'password': '222222',
        }
        response = self.client.post(self.url, data=request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(User.objects.filter(email=request_data['email']).exists(), False)

    def test_validation_error_2(self):
        """ Плохой email """

        request_data = {
            'email': 'test',
        }
        response = self.client.post(self.url, data=request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(email=request_data['email'])

    def test_user_registration_duplicate(self):
        """ Проверка на невозможность повторной регистрации с тем же email """

        request_data = {
            'email': 'user_user_example@test.ru',
            'password': '222fgdf434222',
        }

        # Первая регистрация — должна быть успешной
        response = self.client.post(self.url, data=request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Вторая регистрация с теми же данными — должна вернуть ошибку
        response = self.client.post(self.url, data=request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Проверяем, что ошибка связана с полем email
        self.assertIn('error', response.data)

        # Количество пользователей должно оставаться равным 1
        self.assertEqual(User.objects.count(), 1)

    def test_user_registration_returns_tokens(self):
        """ Успешная регистрация возвращает access и refresh токены """

        request_data = {
            'email': 'user_user_example@test.ru',
            'password': '222fgdf434222',
        }
        response = self.client.post(self.url, data=request_data, format='json')

        # Проверка успешного статуса
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверка, что токены присутствуют в ответе
        self.assertIn('access_token', response.data)
        self.assertIn('refresh_token', response.data)

        # Убедимся, что access и refresh токены не пусты
        access_token = response.data['access_token']
        refresh_token = response.data['refresh_token']

        self.assertIsNotNone(access_token)
        self.assertIsNotNone(refresh_token)
        self.assertNotEqual(access_token, '')
        self.assertNotEqual(refresh_token, '')
