from django.test import TestCase
from user_app.forms import RegistrationForm
from user_app.models import User


class TestRegistrationView(TestCase):
    """ Тест класса регистрации пользователей.
    В этом тесте проверяются: статус-код страницы регистрации,
    наличия формы для регистрации пользователя на странице регистрации
     """

    def test_registration_get(self):
        """ Метод для проверки статус-кода 200 страницы регистрации """
        self.response = self.client.get('/registration/')
        self.assertEqual(self.response.status_code, 200)

    def test_page_reg_form(self):
        """ Метод для проверки наличия формы для регистрации пользователя на странице регистрации """

        self.response = self.client.get('/registration/')
        context = self.response.context
        form_context_name = 'form'
        self.assertIn(form_context_name, context)

        # проверка типа формы
        form = context[form_context_name]
        self.assertEqual(type(form), RegistrationForm)

    def test_registration_post(self):
        """Метод для проверки статус-кода ответа, который возвращается
        при попытке отправки POST-запроса на URL /registration/
        с определенными данными для регистрации пользователя. """

        user_data = {
            'username': 'new_user',
            'email': 'test@test.ru',
            'password1': 'qweRty_1Nv',
            'password2': 'qweRty_1Nv',
        }

        response = self.client.post('/registration/', data=user_data)
        self.assertEqual(response.status_code, 302)

    def test_user_created_check(self):
        """Метод для проверки создания пользователя"""

        user_data = {
            'username': 'new_user',
            'email': 'test@test.ru',
            'password1': 'qweRty_1Nv',
            'password2': 'qweRty_1Nv',
        }
        self.client.post('/registration/', user_data)
        self.assertTrue(User.objects.filter(username='new_user').exists())

    def test_redirect_url(self):
        """Метод для проверки, что после входа осуществляется переадесация"""
        user_data = {
            'username': 'new_user',
            'email': 'test@test.ru',
            'password1': 'qweRty_1Nv',
            'password2': 'qweRty_1Nv',
        }
        response = self.client.post('/registration/', user_data)
        self.assertRedirects(response, '/login/')

    def test_access_to_page_creating_new_course(self):
        """ Метод для проверки наличия разрешения на просмотр страницы
        создания нового курса у авторизованного пользователя"""

        # Проверяем статус-код страницы создания нового курса
        url = '/courses/create/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        # Создаем пользователя
        user = User.objects.create_user(username='tomas_shelbi',
                                        email='tomi@test.ru',
                                        password='Tom_She_MSK')

        # Пользователь авторизуется
        self.client.login(email='tomi@test.ru', password='Tom_She_MSK')

        # Снова делаем запрос и статус должен быть уже 200
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Выходим из аккаунта пользователя
        self.client.logout()

        # Снова запрашиваем статус страницы
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
