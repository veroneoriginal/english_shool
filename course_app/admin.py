import django_rq
from django.contrib import admin
from course_app.models import Course
from .job import save_report_with_courses


# pylint: disable=W0613 unused-argument
class CourseAdmin(admin.ModelAdmin):
    """Класс настройки админки для выгрузки курсов"""

    list_display = ('id', 'name')

    @admin.action(description="Download Course")
    def download_course(self, request, queryset):
        django_rq.enqueue(save_report_with_courses, queryset=queryset)

    actions = [download_course]


admin.site.register(Course, CourseAdmin)
