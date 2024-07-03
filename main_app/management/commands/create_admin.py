from django.core.management import BaseCommand
from user_app.models import User


class Command(BaseCommand):
    help = 'Create superuser'

    def handle(self, *args, **options):

        user_admin = User.objects.filter(username='admin', email='admin123@admin.ru').exists()

        if not user_admin:

            user_admin = User(
                username='admin',
                email='admin123@admin.ru',
                is_superuser=True,
                is_staff=True,
            )

            user_admin.set_password('123')
            user_admin.save()
            self.stdout.write(self.style.SUCCESS('Superuser created!'))
        else:
            self.stdout.write(self.style.WARNING('A user with that username already exists.'))
