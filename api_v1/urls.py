from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter
from api_v1.course.views import CoursesViewSet
from api_v1.teachers.views import TeacherViewSet
from api_v1.user.views import UserRegistrationView

app_name = 'api_v1'
router = DefaultRouter()
router.register(r'courses', CoursesViewSet, basename='courses')
router.register(r'teachers', TeacherViewSet, basename='teachers')

# Подключаем маршруты от роутера
urlpatterns = [
    path('', include(router.urls)),
    path('registration/', UserRegistrationView.as_view(), name='registration'),

]
