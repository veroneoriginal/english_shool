from django.core.management.base import BaseCommand
from faker import Faker
from user_app.models import User, Role


class Command(BaseCommand):
    help = 'Fill db with data'

    def handle(self, *args, **options):
        fake = Faker('ru-ru')
        count_people_for_db = 20

        print('Удаляю всех пользователей, кроме админа ...')
        User.objects.filter(is_superuser=False).delete()

        print('Delete old roles ...')
        Role.objects.all().delete()

        print('Create roles ...')
        role_registration = Role.objects.create(name=Role.REGISTRATION)
        role_student = Role.objects.create(name=Role.STUDENT)
        role_teacher = Role.objects.create(name=Role.TEACHER)

        print('Create users ... ')
        for people in range(count_people_for_db):
            username = fake.user_name()
            email = fake.email()
            phone_number = fake.phone_number()[:15]

            user = User.objects.create_user(
                username=username,
                email=email,
                phone_number=phone_number,
                password='qwerty123',
            )

            # Назначение ролей пользователям
            if people <= 3:
                user.role.add(role_teacher)
            elif 3 < people <= 13:
                user.role.add(role_student)
            else:
                user.role.add(role_registration)
            user.save()

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена пользователями и ролями'))

