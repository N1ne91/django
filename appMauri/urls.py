from django.contrib import admin
from django.urls import path, include
from appMauri import views

urlpatterns = [
    path('', views.index),
    path('pagina2/', views.pagina2),
    
]