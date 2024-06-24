from django.core.management.base import BaseCommand
from faker import Faker
from user_app.models import User


class Command(BaseCommand):
    help = 'Fill db with data'

    def handle(self, *args, **options):

        fake = Faker('ru-ru')
        count_people_for_db = 20

        for people in range(count_people_for_db):
            username = fake.user_name()
            email = fake.email()
            phone_number = fake.phone_number()[:15]
            User.objects.create_user(username=username,
                                     email=email,
                                     phone_number=phone_number,
                                     password='qwerty123')

        self.stdout.write(
            self.style.SUCCESS('Success')
        )
