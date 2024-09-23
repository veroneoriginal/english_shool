from django.contrib.auth.backends import ModelBackend
from user_app.models import User

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Меняем username на email
        email = kwargs.get('email', username)

        try:
            # Ищем пользователя по email
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        # Проверка пароля
        if user.check_password(password):
            return user

        return None
