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

    usuario_id = request.session.get('usuario_id')
    
    if usuario_id:

        usuario = Usuario.objects.get(id=usuario_id)
    else:
        usuario = Usuario.objects.get(nivel='0')
    

    if request.method == "POST" and request.POST.get("novocomun") == "true":
        nick = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        email =request.POST.get("email")

        Usuario.objects.create(nome=nick,cpf=cpf,email=email,ativo=True,nivel=1)


    if request.method == "POST" and request.POST.get("novoadmin") == "true":
        usuario.nome = request.POST.get("nome")
        usuario.cpf = request.POST.get("cpf")
        usuario.email = request.POST.get("email")
        usuario.ativo = request.POST.get("ativo") 
        usuario.nivel = request.POST.get("nivel")
        Usuario.objects.create(nome=usuario.nome,cpf=usuario.cpf,email=usuario.email,ativo=usuario.ativo,nivel=usuario.nivel)
        return redirect('/usuarios')
        
        
    return render(request, "core/cadU.html", {'conta': usuario})
        



  
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



def logout(request):
    if 'usuario_id' in request.session:
        del request.session['usuario_id']
    return redirect('/')


def editar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    conta_id = request.session.get('usuario_id')

    if not conta_id:
        return redirect('/')

    conta = Usuario.objects.get(id=conta_id)

    if request.method == "POST" and request.POST.get("deletar") == "true":
        usuario.delete()
        return redirect('/usuarios')

    if request.method == "POST":
        usuario.nome = request.POST.get("nome")
        usuario.cpf = request.POST.get("cpf")
        usuario.email = request.POST.get("email")
        usuario.ativo = request.POST.get("ativo") 
        usuario.nivel = request.POST.get("nivel")
        usuario.save()
        return redirect('/usuarios')

    return render(request, "core/editar_usuario.html", {'usuario': usuario, 'conta': conta})


