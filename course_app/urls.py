from django.urls import path
from course_app import views

app_name = 'course_app'

urlpatterns = [
    path('courses/', views.CoursesListView.as_view(), name='courses_list'),
    path('courses/<int:pk>/', views.CoursesDetailView.as_view(), name='courses_detail'),
    path('courses/create/', views.CoursesCreateView.as_view(), name='courses_create'),
    path('courses/update/<int:pk>', views.CoursesUpdateView.as_view(), name='courses_update'),
    path('courses/delete/<int:pk>', views.CoursesDeleteView.as_view(), name='courses_delete'),
]
