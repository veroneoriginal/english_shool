from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView
)
from user_app.models import User, Role
from user_app.forms import TeachersForm


class TeachersListView(ListView):
    """Представление страницы со списком преподавателей"""

    model = User
    template_name = 'user_app/teachers_list.html'
    context_object_name = 'users'
    ordering = ['pk']

    def get_queryset(self):
        """Переопределяю метод для получения кверисет"""

        role_teacher = Role.objects.get(name=Role.TEACHER)
        return User.objects.filter(role=role_teacher).prefetch_related('role')
        # return User.objects.filter(role=role_teacher)


class TeachersDetailView(DetailView):
    """Представление страницы просмотра карточки каждого преподавателя"""

    model = User
    template_name = 'user_app/teachers_detail.html'
    context_object_name = 'users'


class TeachersCreateView(CreateView):
    """Представление страницы для внесения нового преподавателя"""

    model = User
    form_class = TeachersForm
    template_name = 'user_app/teachers_form.html'
    success_url = reverse_lazy('user_app:teachers_list')
