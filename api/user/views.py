from rest_framework import status
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
            return Response({
                "error": f"Пользователь с email {email} уже существует."
            },
                status=status.HTTP_400_BAD_REQUEST)

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

        # Возвращаем данные о пользователе и токены
        return Response({
            "user": user.email,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        },
            status=status.HTTP_201_CREATED)
