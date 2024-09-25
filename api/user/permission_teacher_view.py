from rest_framework.permissions import BasePermission

from user_app.models import Role


class IsTeacher(BasePermission):
    """
    Разрешает доступ только пользователям с ролью 'Преподаватель'.
    """

    def has_permission(self, request, view):
        # Проверяем, что пользователь аутентифицирован и имеет роль 'Преподаватель'
        return (request.user.is_authenticated and request.user.role.filter(name=Role.TEACHER).
                exists())
