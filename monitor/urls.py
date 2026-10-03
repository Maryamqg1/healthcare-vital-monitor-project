from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('readings/', views.readings, name='readings'),
    path('add/', views.add_reading, name='add_reading'),
]