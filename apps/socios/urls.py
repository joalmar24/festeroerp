from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear/', views.crear_socio, name='crear_socio'),
    path('editar/<int:pk>/', views.editar_socio, name='editar_socio'),
    path('baja/<int:pk>/', views.baja_socio, name='baja_socio'),
]
