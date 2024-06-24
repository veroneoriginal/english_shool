from django.db import IntegrityError
from django.test import TestCase
from django.core.exceptions import ValidationError
from user_app.models import User, Role

username = "Tom2024"
email = "test@test.ru"
password = "qwerty123"
first_name = "Tom"
last_name = "Doe"
phone_number = "1234567890"


class UserTestCase(TestCase):
    def setUp(self):
        self.role_registered = Role.objects.create(name='registered')
        self.role_student = Role.objects.create(name='student')
        self.role_teacher = Role.objects.create(name='teacher')

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
            email='email@.ru',
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
        self.assertEqual(newuser.email, 'email@.ru')
        # Проверяет, что роль студента находится в списке ролей, связанных с newuser
        self.assertIn(self.role_student, newuser.role.all())

    def test_unique_email(self):
        """Исключение IntegrityError возбуждается, если пытаются создать пользователя
        с уже существующим в бд значением email."""
        with self.assertRaises(IntegrityError):
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
        user = User.objects.create(
            username=username,
            email='invalid-email',
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )
        with self.assertRaises(ValidationError):
            user.full_clean()
            user.save()

    def test_multiple_roles(self):
        """Проверяет, что пользователь может иметь несколько ролей одновременно
        и что роли правильно добавляются к пользователю."""

        # Добавление новой роли пользователю
        self.user.role.add(self.role_student)
        # Проверяет, что роль находится в списке всех ролей пользователя
        self.assertIn(self.role_registered, self.user.role.all())
        self.assertIn(self.role_student, self.user.role.all())
