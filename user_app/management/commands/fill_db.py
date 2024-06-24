from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model
from user_app.models import User


class Command(BaseCommand):
    help = 'Fill db with data'

    def handle(self, *args, **options):
        fake = Faker('ru-ru')
        count_people_for_db = 20

        print('Удаляю всех пользователей, кроме админа ...')
        User.objects.filter(is_superuser=False).delete()

        print('Create users ... ')
        roles = ['registered', 'student', 'teacher']

        for people in range(count_people_for_db):
            username = fake.user_name()
            email = fake.email()
            phone_number = fake.phone_number()[:15]
            role = roles[0]
            if people < 3:
                role = roles[2]
            elif people < 13:
                role = roles[1]

            User.objects.create_user(
                username=username,
                email=email,
                phone_number=phone_number,
                password='qwerty123',
                role=role
            )

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена пользователями и ролями'))

