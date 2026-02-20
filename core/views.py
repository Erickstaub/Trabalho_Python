from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Sala,Usuario,Reserva


# Create your views here.
def home(request):
  salas = Sala.objects.all()
  usuarios = Usuario.objects.all()
  reservas = Reserva.objects.all()
 
   


  return render(request, "core/home.html", {'sala': salas, 'usuario': usuarios, 'reserva': reservas})

def login(request):
     usuarios = Usuario.objects.all()
     if request.method == "POST":
        nick = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        usu = Usuario.objects.get(nome= nick, cpf = cpf)
       
         


     return render(request, "core/login.html", {'usuario': usuarios})

def novoU(request):
   return render(request, "core/cadU.html")