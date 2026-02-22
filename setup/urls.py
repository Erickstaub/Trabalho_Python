"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import editar_usuario, home, login, logout, novoU, menu, salasreservadas, usuarios, salas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , home),
    path('login', login),
    path('menu', menu,name='menu'),
    path('salareservadas',salasreservadas, name='salas-reservadas'),
    path('usuarios', usuarios, name='usuarios'),
    path('salas', salas, name='salas'),
    path('logout', logout, name='logout'),
    path('usuarios/<int:usuario_id>/editar', editar_usuario, name='editar-usuario'),
    path('usuarios/novo', novoU, name='novo-usuario'),
]
