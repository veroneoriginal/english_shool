from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter
from api.course.views import CoursesViewSet
from api.teachers.views import TeacherViewSet

router = DefaultRouter()
router.register(r'courses', CoursesViewSet, basename='courses')
router.register(r'teachers', TeacherViewSet, basename='teachers')

# Подключаем маршруты от роутера
urlpatterns = [
    path('', include(router.urls)),
]
