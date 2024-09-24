from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from api.user.serializers import UserRegistrationViewSerializer
from user_app.models import User, Role


class UserRegistrationView(APIView):
    """ Регистрация пользователя """

    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserRegistrationViewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        # Проверка на существующего пользователя
        if User.objects.filter(email=email).exists():
            raise ValidationError({"email": "Пользователь с таким email уже существует."})

        # Ищем существующую роль "Преподаватель" или создаем, если ее не существует
        # pylint: disable=W0612 unused-variable
        role, created = Role.objects.get_or_create(name=Role.TEACHER)

        # Создаем нового пользователя
        user = User.objects.create(email=email)

        # Безопасное сохранение пароля
        user.set_password(password)
        user.role.add(role)
        user.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # print(refresh,'\n')
        # print(access_token, '\n')
        # print(refresh_token, '\n')

        # Возвращаем данные о пользователе и токены
        return Response({"user": {"email": user.email, },
                         "access_token": access_token,
                         "refresh_token": refresh_token,
                         },
                        status=status.HTTP_201_CREATED)
