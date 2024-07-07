from django.views.generic import (
    TemplateView,
    FormView
)
from .forms import ContactForm
from django.urls import reverse_lazy


class IndexView(TemplateView):
    """Представление главной страницы"""

    template_name = 'main_app/index.html'


class ContactView(FormView):
    """Представление страницы с контактами"""
    form_class = ContactForm
    success_url = reverse_lazy('main_app:index')
    template_name = 'main_app/contacts.html'

    def form_valid(self, form):
        data = form.cleaned_data
        print(data)
        print('MESSAGE', data['message'])
        return super().form_valid(form)

    def form_invalid(self, form):
        data = form.cleaned_data
        print(data)
        print('NOT VALID', data['message'])
        return super().form_invalid(form)
