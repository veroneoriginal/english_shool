from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from user_app.models import User
from api.teachers.serializer import UserSerializer


class TeacherViewSet(ModelViewSet):
    queryset = User.objects.filter(role__name='Преподаватель')
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'delete']:
            # Разрешаем только администраторам создавать, изменять и удалять преподавателей
            return [IsAdminUser()]
        # Для остальных действий (просмотр списка) достаточно аутентификации
        return [IsAuthenticated()]
