from django.views.generic import TemplateView, ListView, DetailView

from user_app.models import Course


class IndexView(TemplateView):
    """Представление главной страницы"""

    template_name = 'user_app/index.html'


class CoursesListView(ListView):
    """Представление страницы со списком курсов"""

    model = Course
    template_name = 'user_app/courses_list.html'
    context_object_name = 'courses'


class CoursesDetailView(DetailView):
    """Представление страницы просмотра каждого курса"""

    model = Course
    template_name = 'user_app/courses_detail.html'
    context_object_name = 'course'
