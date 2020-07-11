from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('consumer/', views.consumer)
]