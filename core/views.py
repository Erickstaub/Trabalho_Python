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
    if request.method == "POST":
        nick = request.POST.get("nome")
        cpf = request.POST.get("cpf")

        usu = Usuario.objects.filter(nome=nick, cpf=cpf).first()

        if usu:
            request.session['usuario_id'] = usu.id
            return redirect('/menu')
        else:
            return render(request, "core/login.html", {
                'erro': 'Usuário ou CPF inválido'
            })

    return render(request, "core/login.html")

def novoU(request):
     
  if request.method == "POST":
        nick = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        email =request.POST.get("email")

        Usuario.objects.create(nome=nick,cpf=cpf,email=email,)
        
        

        



  return render(request, "core/cadU.html")
def menu(request):
    usuario_id = request.session.get('usuario_id')

    if not usuario_id:
        return redirect('/')

    usuario = Usuario.objects.get(id=usuario_id)

    return render(request, "core/menu.html", {'usuario': usuario})

def salasreservadas(request):
     reserva = Reserva.objects.all()
     return render(request, "core/salasreservas.html", {'reserva': reserva})

def usuarios(request):
    usuario_id = request.session.get('usuario_id')

    if not usuario_id:
        return redirect('/')

    usuario = Usuario.objects.get(id=usuario_id)
    usuarios = Usuario.objects.all()
    return render(request, "core/usuarios.html", {'usuarios': usuarios, 'conta': usuario})

def salas(request):
    salas = Sala.objects.all()
    return render(request, "core/salas.html", {'salas': salas})


