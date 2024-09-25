from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter
from api.course.courses_views import CoursesViewSet
from api.users.teachers_views import TeacherViewSet
from api.authentication.registration_views import UserRegistrationView
from api.authentication.login_views import UserLoginView


app_name = 'api'
router = DefaultRouter()
router.register(r'courses', CoursesViewSet, basename='courses')
router.register(r'teachers', TeacherViewSet, basename='teachers')

# Подключаем маршруты от роутера
urlpatterns = [
    path('', include(router.urls)),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),

]
