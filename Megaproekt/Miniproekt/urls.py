from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.login, name='login'),
    path('main/', views.main, name='main'),
    path('tasks/', views.tasks),
    path('team/', views.team),
    path('me/', views.me),
    path('logout/', views.logout),
]