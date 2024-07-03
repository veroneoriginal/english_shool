from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.urls import reverse_lazy
from user_app.models import Course


class IndexView(TemplateView):
    """Представление главной страницы"""

    template_name = 'user_app/index.html'


class CoursesListView(ListView):
    """Представление страницы со списком курсов"""

    model = Course
    template_name = 'user_app/courses_list.html'
    context_object_name = 'courses'
    ordering = ['pk']


class CoursesDetailView(DetailView):
    """Представление страницы просмотра каждого курса"""

    model = Course
    template_name = 'user_app/courses_detail.html'
    context_object_name = 'course'


class CoursesCreateView(CreateView):
    """Представление страницы для создания нового курса"""

    model = Course
    fields = "__all__"
    success_url = reverse_lazy('user_app:courses_list')


class CoursesUpdateView(UpdateView):
    """Представление страницы для обновления информации в карточке курса"""
    model = Course
    fields = "__all__"
    success_url = reverse_lazy('user_app:courses_list')
