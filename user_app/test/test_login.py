from django.test import TestCase


class TestAuthView(TestCase):
    """ Тест класса авторизации пользователей """

    def test_login_get(self):
        """ Проверка ответа страницы статус 200 """

        self.response = self.client.get('/login/')
        self.assertEqual(self.response.status_code, 200)
