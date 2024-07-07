from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView
)
from .models import User
from .forms import UserForm


class TeachersListView(ListView):
    """Представление страницы со списком преподавателей"""

    model = User
    template_name = 'user_app/teachers_list.html'
    context_object_name = 'users'
    ordering = ['pk']


class TeachersDetailView(DetailView):
    """Представление страницы просмотра карточки каждого преподавателя"""

    model = User
    template_name = 'user_app/teachers_detail.html'
    context_object_name = 'users'


class TeachersCreateView(CreateView):
    """Представление страницы для внесения нового преподавателя"""

    model = User
    form_class = UserForm
    success_url = reverse_lazy('user_app:teachers_list')
