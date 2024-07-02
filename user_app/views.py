from django.views.generic import TemplateView, ListView


class IndexView(TemplateView):
    """Главная страница"""
    template_name = 'user_app/index.html'


class CoursesListView(ListView):
    """Страница со списком курсов"""
    template_name = 'user_app/courses_list.html'
