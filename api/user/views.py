from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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

        # Создаем JWT-токены для нового пользователя
        token_serializer = TokenObtainPairSerializer(data={
            "username": email,
            "password": password,
        }
        )

        # token_serializer.is_valid(raise_exception=True)
        # # Это словарь с access и refresh токенами
        # tokens = token_serializer.validated_data
        #
        # print({"username": email, "password": password})  # Выведем данные для отладки

        # # Возвращаем токены и информацию о пользователе
        # return Response({
        #     "user": serializer.data,  # данные пользователя
        #     "tokens": tokens,  # access и refresh токены
        # }, status=status.HTTP_201_CREATED)


        return Response({"user": serializer.data}, status=status.HTTP_201_CREATED)
