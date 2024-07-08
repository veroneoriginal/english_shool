from django.urls import path
from user_app import views

app_name = 'user_app'

urlpatterns = [
    path('teachers/', views.TeachersListView.as_view(), name='teachers_list'),
    path('teachers/<int:pk>/', views.TeachersDetailView.as_view(), name='teachers_detail'),
    path('teachers/create/', views.TeachersCreateView.as_view(), name='teachers_create'),
]
