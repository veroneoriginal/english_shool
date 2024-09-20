from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.user.serializers import UserRegistrationViewSerializer
from user_app.models import User, Role


class UserRegistrationView(APIView):
    """ Регистрация пользователя """

    def post(self, request):
        serializer = UserRegistrationViewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        role = Role.objects.create(name=Role.TEACHER)

        user = User.objects.create(email=email, password=password)
        user.role.add(role)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
