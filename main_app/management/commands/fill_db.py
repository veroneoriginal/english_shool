import random

from django.core.management.base import BaseCommand
from faker import Faker
from user_app.models import User, Role


class Command(BaseCommand):
    help = 'Fill db with data - teachers and students'

    def handle(self, *args, **options):
        fake = Faker('ru-ru')
        count_people_for_db = 20

        print('Удаляю всех пользователей, кроме админа ...')
        User.objects.filter(is_superuser=False).delete()

        print('Delete old roles ...')
        Role.objects.all().delete()

        print('Create roles ...')
        # role_registration = Role.objects.create(name=Role.REGISTRATION)
        role_student = Role.objects.create(name=Role.STUDENT)
        role_teacher = Role.objects.create(name=Role.TEACHER)

        possible_roles = [role_student, role_teacher]

        print('Create users ... ')
        for _ in range(count_people_for_db):
            username = fake.user_name()
            email = fake.email()
            phone_number = fake.phone_number()[0:11]

            user = User.objects.create_user(
                username=username,
                email=email,
                phone_number=phone_number,
                password='qwerty123',
            )
            # user.role.add(role_registration)

            # Назначение случайной второй роли из списка возможных с вероятностью 70%
            user.role.add(random.choice(possible_roles))

            user.save()

        self.stdout.write(self.style.
                          SUCCESS('База данных успешно заполнена пользователями и ролями'))
