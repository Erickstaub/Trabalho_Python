from django.shortcuts import render
from django.shortcuts import render, redirect

from .models import Sala,Usuario,Reserva


# Create your views here.
def home(request):
   try:
    usuario_id = request.session.get('usuario_id')
    usuario = Usuario.objects.get(id=usuario_id)

   except Usuario.DoesNotExist:
        usuario = None



   return render(request, "core/home.html", {'conta': usuario})

def login(request):
    if request.method == "POST":
        nick = request.POST.get("nome")
        cpf = request.POST.get("cpf")

        usu = Usuario.objects.filter(nome=nick, cpf=cpf, ativo=True).first()

        if usu:
            request.session['usuario_id'] = usu.id
     
            return redirect('/menu')
        else:
            return render(request, "core/login.html", {'error': 'Usuário ou CPF inválidos.'})

    return render(request, "core/login.html")

def novoU(request):

    try:
         usuario_id = request.session.get('usuario_id')
         usuario = Usuario.objects.get(id=usuario_id)

    except Usuario.DoesNotExist:
          usuario = None


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
    try:
        usuario_id = request.session.get('usuario_id')
        usuario = Usuario.objects.get(id=usuario_id)

    except Usuario.DoesNotExist:
        usuario = None
        return redirect('/')

    return render(request, "core/menu.html", {'conta': usuario})

def salas(request):
     reserva = Reserva.objects.all()
     return render(request, "core/salasreservas.html", {'reserva': reserva})

def usuarios(request):
    try:
        usuario_id = request.session.get('usuario_id')
        usuario = Usuario.objects.get(id=usuario_id)

    except Usuario.DoesNotExist:
        usuario = None
        return redirect('/')

   
    usuarios = Usuario.objects.all()

    return render(request, "core/usuarios.html", {'usuarios': usuarios, 'conta': usuario})


def salas(request):
    try:
        usuario_id = request.session.get('usuario_id')
        usuario = Usuario.objects.get(id=usuario_id)

    except Usuario.DoesNotExist:
        usuario = None
        return redirect('/')
    
    salas = Sala.objects.all()





    return render(request, "core/salas.html", {'salas': salas, 'conta': usuario})

def criar_sala(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        capacidade = request.POST.get("capacidade")
        Sala.objects.create(nome=nome, capacidade=capacidade)
        return redirect('/salas')

    return render(request, "core/criarS.html")



def logout(request):
    if 'usuario_id' in request.session:
        del request.session['usuario_id']
    return redirect('/')


def editar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    try:
        conta_id = request.session.get('usuario_id')
        conta = Usuario.objects.get(id=conta_id)

    except Usuario.DoesNotExist:
        conta = None
        return redirect('/')

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


def editar_conta(request, conta_id):
    conta = Usuario.objects.get(id=conta_id)
    

    if not conta:
        return redirect('/')

  

    if request.method == "POST" and request.POST.get("deletar") == "true":
        conta.delete()
        return redirect('/usuarios')

    if request.method == "POST":
        conta.nome = request.POST.get("nome")
        conta.email = request.POST.get("email")
        conta.foto_perfil = request.POST.get("foto_perfil")
        if conta.foto_perfil == "":
            conta.foto_perfil = None
        conta.save()
        return redirect('/menu')

    return render(request, "core/settings.html", {'conta': conta})