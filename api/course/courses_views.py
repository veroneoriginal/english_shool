from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from api.course.serializer import CourseSerializer
from api.user.permission_teacher_view import IsTeacher
from course_app.models import Course


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            # Разрешаем просмотр курсов всем (включая неаутентифицированных)
            return [IsAuthenticatedOrReadOnly()]
        # Для создания, изменения и удаления курсов разрешаем доступ только преподавателям
        return [IsAuthenticated(), IsTeacher()]
