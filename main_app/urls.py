from django.urls import path
from main_app import views

app_name = 'main_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contacts/', views.ContactView.as_view(), name='contacts'),
]
