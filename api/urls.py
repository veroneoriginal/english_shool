from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter
from api.views import CoursesViewSet

router = DefaultRouter()
router.register(r'courses', CoursesViewSet, basename='courses')

# Подключаем маршруты от роутера
urlpatterns = [
    path('', include(router.urls)),
]
