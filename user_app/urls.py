from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('courses/list/', views.CoursesListView.as_view(), name='courses_list'),
]
