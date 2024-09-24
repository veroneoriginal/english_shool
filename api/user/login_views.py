from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from api.user.serializers import UserLoginViewSerializer
from user_app.models import User


class UserLoginView(APIView):
    """ Аутентификация пользователя """

    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserLoginViewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        # Проверка, существует ли пользователь с указанным email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Пользователь с таким email не найден.'},
                            status=status.HTTP_401_UNAUTHORIZED)

        # Аутентификация пользователя с проверкой пароля
        user = authenticate(request, username=email, password=password)

        if user:
            # Генерация JWT токенов
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                'access_token': access_token,
                'refresh_token': refresh_token
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Неверный пароль.'},
                        status=status.HTTP_401_UNAUTHORIZED)
