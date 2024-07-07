from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from course_app.models import Course
from course_app.forms import CourseForm


class CoursesListView(ListView):
    """Представление страницы со списком курсов"""

    model = Course
    template_name = 'course_app/courses_list.html'
    context_object_name = 'courses'
    ordering = ['pk']


class CoursesDetailView(DetailView):
    """Представление страницы просмотра каждого курса"""

    model = Course
    template_name = 'course_app/courses_detail.html'
    context_object_name = 'course'


class CoursesCreateView(CreateView):
    """Представление страницы для создания нового курса"""

    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('course_app:courses_list')


class CoursesUpdateView(UpdateView):
    """Представление страницы для обновления информации в моделе курса"""

    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('course_app:courses_list')


class CoursesDeleteView(DeleteView):
    """Представление страницы для удаления модели курса"""

    model = Course
    fields = "__all__"
    template_name = 'course_app/courses_confirm_delete.html'
    success_url = reverse_lazy('course_app:courses_list')
