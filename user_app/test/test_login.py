from django.test import TestCase


class LoginTestCase(TestCase):
    """ Класс, отвечающий за авторизацию пользователя """

    def test_login_get(self):
        self.response = self.client.get('/users/login/')
        # проверяем - отвечает ли страница - статус 200
        self.assertEqual(self.response.status_code, 200)


