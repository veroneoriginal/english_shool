from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('courses/', views.CoursesListView.as_view(), name='courses_list'),
    path('courses/<int:pk>/', views.CoursesDetailView.as_view(), name='courses_detail'),
    path('courses/create/', views.CoursesCreateView.as_view(), name='courses_create'),
    path('courses/update/<int:pk>', views.CoursesUpdateView.as_view(), name='courses_update'),
]
