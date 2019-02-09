from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregarUsuario/', views.agregar_usuario, name='agregarUsuario'),
    path('registrarUsuario/', views.registrar_usuario, name='registrarUsuario'),
]