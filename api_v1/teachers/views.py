from rest_framework.viewsets import ModelViewSet
from user_app.models import User
from api_v1.teachers.serializer import UserSerializer

class TeacherViewSet(ModelViewSet):
    queryset = User.objects.filter(role__name='Преподаватель')
    serializer_class = UserSerializer
