# weather_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weatherApp.urls')),  # Include the app's URL configuration
]