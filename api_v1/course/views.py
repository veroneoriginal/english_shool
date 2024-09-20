from rest_framework import viewsets
from api_v1.course.serializer import CourseSerializer
from course_app.models import Course


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
