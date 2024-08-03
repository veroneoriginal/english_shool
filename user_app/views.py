from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    DetailView
)
from user_app.models import User, Role
from user_app.forms import TeachersForm, RegistrationForm


class RegisterView(CreateView):
    """Представление страницы для регистрации нового пользователя"""
    model = User
    template_name = 'user_app/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('user_app:login')


class AuthView(LoginView):
    template_name = 'user_app/login.html'


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


class TeachersCreateView(LoginRequiredMixin, CreateView):
    """Представление страницы для внесения нового преподавателя"""

    model = User
    form_class = TeachersForm
    template_name = 'user_app/teachers_form.html'
    success_url = reverse_lazy('user_app:teachers_list')

    # Дополнительно можно указать URL для перенаправления, если пользователь не авторизован
    login_url = '/login/'  # URL на страницу входа
    redirect_field_name = 'next'  # Параметр для перенаправления после успешного входа

