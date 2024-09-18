import django_rq
from django.views.generic import (
    TemplateView,
    FormView
)
from django.urls import reverse_lazy
from main_app.forms import ContactForm
from main_app.job import send_email_to_admin, send_confirmation_email


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
        # print(data)

        email = data['email']
        message = data['message']
        # print('MESSAGE', data['message'])

        # Добавление задач в очередь
        django_rq.enqueue(send_email_to_admin, email, message)
        django_rq.enqueue(send_confirmation_email, email)

        return super().form_valid(form)

    def form_invalid(self, form):
        data = form.cleaned_data
        print(data)
        print('NOT VALID', data['message'])
        return super().form_invalid(form)
