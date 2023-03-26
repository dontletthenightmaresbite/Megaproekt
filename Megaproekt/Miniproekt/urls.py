from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('main/', views.main),
    path('tasks/', views.tasks),
    path('team/', views.team),
    path('me/', views.me),
]