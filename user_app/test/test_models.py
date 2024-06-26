from django.test import TestCase
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from user_app.models import User, Role
from user_app.errors import CreateRoleExeption

username = "Tom2024"
email = "test@test.ru"
password = "qwerty123"
first_name = "Tom"
last_name = "Doe"
phone_number = "1234567890"


class UserTestCase(TestCase):
    def setUp(self):
        self.role_registered = Role.objects.create(name=Role.REGISTRATION)
        self.role_student = Role.objects.create(name=Role.STUDENT)
        self.role_teacher = Role.objects.create(name=Role.TEACHER)

        self.user = User.objects.create(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

        self.user.role.add(self.role_registered)

    def test_create_user(self):
        """Проверяет, что пользователь был успешно создан в бд"""
        self.assertTrue(User.objects.exists())

    def test_create_user_count(self):
        """Проверяет, что в бд существует ровно один пользователь."""
        self.assertEqual(User.objects.count(), 1)

    def test_create_user_field_value(self):
        """Проверяет, что значения полей созданного пользователя соответствуют
        ожидаемым значениям, а также что у пользователя назначена роль registered"""
        self.assertEqual(self.user.username, username)
        self.assertEqual(self.user.email, email)
        self.assertEqual(self.user.password, password)
        self.assertEqual(self.user.first_name, first_name)
        self.assertEqual(self.user.last_name, last_name)
        self.assertEqual(self.user.phone_number, phone_number)
        self.assertIn(self.role_registered, self.user.role.all())

    def test_nonunique_username(self):
        """Проверяет, что можно создать пользователя с неуникальным username,
        но с уникальным email, и что ему правильно назначается роль student."""
        newuser = User.objects.create(
            username=username,
            email='email@example.ru',
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

        # Этот метод устанавливает пароль для объекта newuser, используя хеширование
        newuser.set_password(password)
        newuser.save()
        # Это создаёт связь между пользователем и ролью в таблице связи Many-to-Many.
        newuser.role.add(self.role_student)
        # Проверка соответствия email
        self.assertEqual(newuser.email, 'email@example.ru')
        # Проверяет, что роль студента находится в списке ролей, связанных с newuser
        self.assertIn(self.role_student, newuser.role.all())

    def test_unique_email(self):
        """Исключение IntegrityError возбуждается, если пытаются создать пользователя
        с уже существующим в бд значением email."""
        with self.assertRaises(ValidationError):
            User.objects.create(
                username='another_username',
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
            )

    def test_fail_email(self):
        """Исключение ValidationError возбуждается, если
        email пользователя является недействительным (не соот.формату email)."""
        with self.assertRaises(ValidationError):
            User.objects.create(
                username=username,
                email='invalid-email',
                password=password,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
            )

    def test_multiple_roles(self):
        """Проверяет, что пользователь может иметь несколько ролей одновременно
        и что роли правильно добавляются к пользователю."""

        # Добавление новой роли пользователю
        self.user.role.add(self.role_student)
        # Проверяет, что роль находится в списке всех ролей пользователя
        self.assertIn(self.role_registered, self.user.role.all())
        self.assertIn(self.role_student, self.user.role.all())
        self.assertEqual(self.user.role.count(), 2)

    def test_create_invalid_role(self):
        """Проверяет, что создание роли с недопустимым значением вызывает исключение"""

        with self.assertRaises(CreateRoleExeption):
            Role.objects.create(name='invalid_role')

        with self.assertRaises(ObjectDoesNotExist):
            Role.objects.get(name='invalid_role')
