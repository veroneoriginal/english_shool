from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from user_app.models import User
from api.teachers.serializer import UserSerializer

class TeacherViewSet(ModelViewSet):
    queryset = User.objects.filter(role__name='Преподаватель')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
