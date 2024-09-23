from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.course.serializer import CourseSerializer
from course_app.models import Course


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
