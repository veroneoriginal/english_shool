from django.core.mail import send_mail
from django.conf import settings

def send_email_to_admin(email, message):
    """Отправляет письмо администратору о новом сообщении"""

    send_mail(
        'Новое сообщение от пользователя',
        f'Email: {email}\n\nСообщение:\n{message}',
        settings.DEFAULT_FROM_EMAIL,
        ['admin123@admin.ru'],
        fail_silently=False,
    )

def send_confirmation_email(email):
    """Отправляет подтверждение пользователю, что сообщение получено"""

    send_mail(
        'Ваше сообщение получено',
        'Спасибо за ваше сообщение. Мы свяжемся с вами в ближайшее время.',
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
