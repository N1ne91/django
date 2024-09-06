from django.urls import path
from . import views

urlpatterns = [
    path('sueño/', views.pregunta),
    path('presentacion/', views.presentacion),


]