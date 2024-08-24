import time


def save_report_with_courses(queryset):
    time.sleep(5)
    with open('courses.txt', 'w', encoding='utf-8') as f:
        for course in queryset.all():
            f.write(f'{course}\n')
