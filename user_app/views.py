from django.views.generic import TemplateView, ListView

from user_app.models import Course


class IndexView(TemplateView):
    """Главная страница"""
    template_name = 'user_app/index.html'


class CoursesListView(ListView):
    """Страница со списком курсов"""
    model = Course
    template_name = 'user_app/courses_list.html'
    context_object_name = 'courses'
