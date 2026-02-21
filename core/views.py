from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Sala,Usuario,Reserva


# Create your views here.
def home(request):
  salas = Sala.objects.all()
  usuarios = Usuario.objects.all()
  reservas = Reserva.objects.all()
 
   


  return render(request, "core/base.html", {'sala': salas, 'usuario': usuarios, 'reserva': reservas})

def login(request):
     usuarios = Usuario.objects.all()
     if request.method == "POST":
        nick = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        usu = Usuario.objects.get(nome= nick, cpf = cpf)
        if usu:
            return redirect('/menu')
         


     return render(request, "core/login.html", {'usuario': usuarios})

def novoU(request):
     
  if request.method == "POST":
        nick = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        email =request.POST.get("email")

        Usuario.objects.create(nome=nick,cpf=cpf,email=email,)
        
        

        



  return render(request, "core/cadU.html")
def menu(request):
     
  if request.method == "POST":
        nick = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        email =request.POST.get("email")

        Usuario.objects.create(nome=nick,cpf=cpf,email=email,)
        
        

        



  return render(request, "core/menu.html")

def salasreservadas(request):
     reserva = Reserva.objects.all()
     return render(request, "core/salasreservas.html", {'reserva': reserva})


