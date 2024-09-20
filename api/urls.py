from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api.course.views import CoursesViewSet
from api.teachers.views import TeacherViewSet
from api.user.views import UserRegistrationView
from api.user_auth.views import UserAuthenticationView

router = DefaultRouter()
router.register(r'courses', CoursesViewSet, basename='courses')
router.register(r'teachers', TeacherViewSet, basename='teachers')

# Подключаем маршруты от роутера
urlpatterns = [
    path('', include(router.urls)),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('auth/', UserAuthenticationView.as_view(), name='auth')

]
