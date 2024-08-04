from django.test import TestCase
from user_app.forms import RegistrationForm
from user_app.models import User


class TestRegistrationView(TestCase):
    """ Класс - использует get в запросе """

    def setUp(self):
        self.response = self.client.get('/registration/')

    def test_registration_get(self):
        # проверяем - отвечает ли страница - статус 200
        self.assertEqual(self.response.status_code, 200)

    def test_page_contains_reg_form(self):
        # есть ли на странице форма регистрации
        context = self.response.context
        form_context_name = 'form'
        self.assertIn(form_context_name, context)

        # проверка типа формы
        form = context[form_context_name]
        self.assertEqual(type(form), RegistrationForm)


class TestRegistrationPostView(TestCase):
    """ Класс - использует post в запросе """

    def setUp(self):
        data = {
            'username': 'new_user',
            'email': 'test@test.ru',
            'password1': 'qweRty_1Nv',
            'password2': 'qweRty_1Nv',
        }
        self.response = self.client.post('/registration/', data)

    def test_post_status_code(self):
        # Этот тест проверяет статус-код ответа, который возвращается
        # при попытке отправки POST-запроса на URL /users/register/
        # с определенными данными для регистрации пользователя.

        self.assertEqual(self.response.status_code, 302)

    def test_user_created(self):
        # Проверяем, что пользователь создан
        self.assertTrue(User.objects.filter(username='new_user').exists())

    def test_redirect_url(self):
        self.assertRedirects(self.response, '/login/')


class TestRegistrationPermissions(TestCase):
    """ Есть ли разрешение на просмотр определенных страниц у авторизованного пользователя """

    def test_status_code(self):
        # Проверяем статус-код
        url = '/courses/create/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        # создание пользователя
        user = User.objects.create_user(username='tomas_shelbi',
                                        email='tomi@test.ru',
                                        password='Tom_She_MSK')

        # быстрая авторизация пользователя
        self.client.login(email='tomi@test.ru', password='Tom_She_MSK')

        # снова делаем запрос и статус должен быть уже 200
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # выходим
        self.client.logout()

        # запрашиваем статус страницы
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
