from rest_framework import status
from rest_framework.test import APITestCase
from mixer.backend.django import mixer
from user_app.models import User, Role


class TestTeacherViewSet(APITestCase):
    """ Тесты для вьюшки TeacherViewSet """

    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            username='testuser',
            password='Testpassword123'
        )

        self.url = '/api/teachers/'

        self.teacher_role = Role.objects.create(name='Преподаватель')

        # Создаем 10 преподавателей с помощью mixer
        for _ in range(10):
            teacher = mixer.blend(User)
            teacher.role.add(self.teacher_role)

    def test_unidentified_user_does_not_receive_a_list_of_teachers(self):
        """ НЕаутентифицированный пользователь НЕполучает список преподавателей """

        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_receives_a_list_of_teachers(self):
        """ Аутентифицированный пользователь получает список преподавателей """

        # Аутентифицируем пользователя перед запросом
        self.client.force_authenticate(user=self.user)

        # Выполняем GET-запрос
        response = self.client.get(self.url, format='json')

        # Проверяем статус ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 10)

    def test_user_cannot_create_teacher(self):
        """ Обычный пользователь НЕ может создать преподавателя (POST запрос) """

        # Аутентифицируем пользователя перед запросом
        self.client.force_authenticate(user=self.user)

        # Данные для создания нового преподавателя
        data = {
            'email': 'newteacher@example.com',
            'username': 'newteacher',
            'password': 'NewTeacherPassword123'
        }

        # Пытаемся отправить POST-запрос для создания преподавателя
        response = self.client.post(self.url, data)

        # Проверяем, что пользователь не может создать преподавателя
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
