from rest_framework import status
from rest_framework.test import APITestCase
from user_app.models import User


class TestUserRegistrationView(APITestCase):
    """
    Тесты для вьюшки UserLoginView (аутентификация пользователя)
    """

    def setUp(self):
        """ Создание пользователя и ссылки для тестирования аутентификации """

        self.url = '/api/login/'
        self.user = User.objects.create_user(
            email='testuser@example.com',
            username='testuser',
            password='Testpassword123'
        )

    def test_user_login_successful(self):
        """ Успешная аутентификация пользователя """
        data = {
            'email': 'testuser@example.com',
            'password': 'Testpassword123'
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что access и refresh токены присутствуют в ответе
        self.assertIn('access_token', response.data)
        self.assertIn('refresh_token', response.data)

    def test_user_login_wrong_password(self):
        """ Аутентификация с неправильным паролем должна вернуть 401 """

        data = {
            'email': 'testuser@example.com',
            'password': 'Wrongpassword'
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], 'Неверные логин или пароль.')

    def test_user_login_non_existent_email(self):
        """ Аутентификация с несуществующим email должна вернуть 401 """

        data = {
            'email': 'nonexistent@example.com',
            'password': 'Testpassword123'
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], 'Неверные логин или пароль.')

    def test_user_login_missing_email(self):
        """ Запрос без email должен вернуть ошибку 400 """

        data = {
            'password': 'Testpassword123'
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Проверка, что в ответе есть ошибка по полю 'email'
        self.assertIn('email', response.data)
        self.assertEqual(response.data['email'][0], 'Обязательное поле.')


    def test_user_login_missing_password(self):
        """ Запрос без пароля должен вернуть ошибку 400 """

        data = {
            'email': 'testuser@example.com',
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Проверка, что в ответе есть ошибка по полю 'password'
        self.assertIn('password', response.data)
        self.assertEqual(response.data['password'][0], 'Обязательное поле.')


    def test_is_there_user_in_database(self):
        """ Проверяем появился ли созданный пользователь в базе данных"""

        # Проверяем, существует ли пользователь с данным email в базе
        user_in_db = User.objects.filter(email='testuser@example.com').exists()

        # Проверяем, что пользователь действительно был создан и находится в базе данных
        self.assertTrue(user_in_db, "Пользователь не был найден в базе данных.")
