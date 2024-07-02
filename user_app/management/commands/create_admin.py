from django.core.management import BaseCommand
from user_app.models import User


class Command(BaseCommand):
    help = 'Create superuser'

    def handle(self, *args, **options):

        user_admin, created = User.objects.get_or_create(username='admin', defaults={
            'email': 'admin123@admin.ru',
            'is_superuser': True,
            'is_staff': True,
        })

        if created:
            user_admin.set_password('123')
            user_admin.save()
            self.stdout.write(self.style.SUCCESS('Superuser created!'))
        else:
            self.stdout.write(self.style.WARNING('A user with that username already exists.'))
