from django.db import IntegrityError
from django.test import TestCase
from user_app.models import User

username = "Tom2024",
email = "test@test.ru",
password = "qwerty123",
first_name = "Tom",
last_name = "Doe",
phone_number = "1234567890"


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

    def test_create_user(self):
        self.assertTrue(User.objects.exists())

    def test_create_user_count(self):
        self.assertEqual(User.objects.count(), 1)

    def test_create_user_field_value(self):
        self.assertEqual(self.user.username, username)
        self.assertEqual(self.user.email, email)
        self.assertEqual(self.user.password, password)
        self.assertEqual(self.user.first_name, first_name)
        self.assertEqual(self.user.last_name, last_name)
        self.assertEqual(self.user.phone_number, phone_number)

    def test_nounique_username(self):
        newuser = User.objects.create(
            username=username,
            email='email@.ru',
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

        self.assertEqual(newuser.email, 'email@.ru')

    def test_unique_email(self):
        with self.assertRaises(IntegrityError):
            newuser = User.objects.create(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
            )

    def test_validation_email(self):
        newuser = User.objects.create(
            username=username,
            email='email',
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )
