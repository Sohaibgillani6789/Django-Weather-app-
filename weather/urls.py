from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('weather/<str:city>/', views.city_weather, name='city_weather'),  # City-specific weather
    path('search/', views.search_weather, name='search_weather'),  # Search endpoint
]
