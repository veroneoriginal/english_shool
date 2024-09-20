from rest_framework.views import APIView
from rest_framework.response import Response


class UserAuthenticationView(APIView):
    """ Аутентификация пользователя через браузер"""

    def get(self, request):
        user = request.user  # Получаем аутентифицированного пользователя
        return Response({
            'message': 'You are authenticated',
            'username': user.username,
            'email': user.email
        })
