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
from core.views import deletar_recurso,criar_recurso, gerenciar_reserva, minhas_reservas, recursos, reservas, criar_sala, editar_conta, editar_sala, editar_usuario, home, login, logout, novoU, menu, salas, usuarios, salas, reservar_sala

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , home),
    path('login', login),
    path('menu', menu,name='menu'),
    path('salareservadas',salas, name='salas-reservadas'),
    path('usuarios', usuarios, name='usuarios'),
    path('salas', salas, name='salas'),
    path('logout', logout, name='logout'),
    path('usuarios/<int:usuario_id>/editar', editar_usuario, name='editar-usuario'),
    path('usuarios/novo', novoU, name='novo-usuario'),
    path('usuarios/<int:conta_id>/settings', editar_conta, name='editar-conta'),
    path('salas/criar', criar_sala, name='criar-sala'),
    path('salas/<int:sala_id>/editar', editar_sala, name='editar-sala'),
    path('salas/<int:sala_id>/reservar', reservar_sala, name='reservar-sala'),
    path('reservas', reservas, name='reservas'),
    path('reservas/<int:reserva_id>/gerenciar', gerenciar_reserva, name='gerenciar-reserva'),
    path('reservas/myself', minhas_reservas, name='minhas-reservas'),
    path('recursos', recursos, name='recursos'),
    path('recursos/criar', criar_recurso, name='criar-recurso'),
    path('recursos/<int:recurso_id>/deletar', deletar_recurso, name='deletar-recurso'),
    
]
