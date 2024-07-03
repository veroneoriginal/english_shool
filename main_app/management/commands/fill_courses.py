from django.core.management.base import BaseCommand
from main_app.models import Course
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Create courses'

    def handle(self, *args, **options):

        print('Создаю курсы ...')
        course_names = ['Русский', 'Английский', 'Французский', 'Испанский', 'Португальский', 'Китайский']
        random.shuffle(course_names)  # Перемешивание списка курсов для случайного порядка

        for course_name in course_names:
            description = f"Это описание для курса {course_name}."
            start_date = date.today() + timedelta(days=random.randint(1, 30))
            end_date = start_date + timedelta(days=random.randint(30, 90))

            Course.objects.create(
                name=course_name,
                description=description,
                start_date=start_date,
                end_date=end_date
            )

        self.stdout.write(self.style.SUCCESS('Курсы успешно созданы'))
