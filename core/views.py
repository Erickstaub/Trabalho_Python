from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Sala,Usuario,Reserva


# Create your views here.
def home(request):
  salas = Sala.objects.all()
  usuarios = Usuario.objects.all()
  reservas = Reserva.objects.all()
 
   


  return render(request, "core/home.html", {'sala': salas, 'usuario': usuarios, 'reserva': reservas})
