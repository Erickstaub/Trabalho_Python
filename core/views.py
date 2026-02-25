import decimal

from django.shortcuts import render
from django.shortcuts import render, redirect

from .models import Sala,Usuario,Reserva,Recurso


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
        return redirect('/login')


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
    try:
        usuario_id = request.session.get('usuario_id')
        usuario = Usuario.objects.get(id=usuario_id)

    except Usuario.DoesNotExist:
        usuario = None
        return redirect('/')
    sala = Sala.objects.all()
    recursos = Recurso.objects.all()
    if request.method == "POST":
        numsala = request.POST.get("numsala")
        capacidade = request.POST.get("capacidade")
        preco = request.POST.get("preco")
        disponivel = request.POST.get("disponivel") == "on"
        dia_nao_disponivel = request.POST.get("dia_nao_disponivel")
        recu = request.POST.getlist("recursos")
        sala = Sala.objects.create(numsala=numsala,capacidade=capacidade,preco=preco,disponivel=True,dia_nao_disponivel=dia_nao_disponivel)
        for recurso_id in recu:
            recurso = Recurso.objects.get(id=recurso_id)
            sala.recursos.add(recurso)

        


        return redirect('/salas')

    return render(request, "core/criarS.html", {'conta': usuario, 'salas': sala , 'recursos': recursos})



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
from django.shortcuts import render, get_object_or_404, redirect
from .models import Sala

def editar_sala(request, sala_id):
    try:
        conta_id = request.session.get('usuario_id')
        conta = Usuario.objects.get(id=conta_id)

    except Usuario.DoesNotExist:
        conta = None
        return redirect('/')

    sala = get_object_or_404(Sala, id=sala_id)

    recursoss = Recurso.objects.all()
    if request.method == "POST":
        sala.numsala = request.POST.get("numsala")
        sala.capacidade = request.POST.get("capacidade")
        sala.preco = request.POST.get("preco")
        sala.dia_nao_disponivel = request.POST.get("dia_nao_disponivel")
        sala.disponivel = request.POST.get("disponivel") == "on"
        recu = request.POST.getlist("recursos")
        sala.recursos.set(recu)
        sala.save()
        return redirect("salas") 

    return render(request, "core/editarS.html", {"sala": sala , "recursos": recursoss , 'conta': conta}) 

def reservar_sala(request, sala_id):
    try:
        conta_id = request.session.get('usuario_id')
        conta = Usuario.objects.get(id=conta_id)

    except Usuario.DoesNotExist:
        conta = None
        return redirect('/')

    sala = get_object_or_404(Sala, id=sala_id)

    if request.method == "POST":
        data_reserva = request.POST.get("data_reserva")
        hora_inicio = request.POST.get("hora_inicio")
        hora_fim = request.POST.get("hora_fim")
        preco = sala.preco
        multas = 0.00

        if hora_inicio >= hora_fim:
            return render(request, "core/reservar.html", {"sala": sala , 'conta': conta, 'error': 'A hora de início deve ser anterior à hora de término.'})
        if data_reserva == str(sala.dia_nao_disponivel):
            return render(request, "core/reservar.html", {"sala": sala , 'conta': conta, 'error': 'A sala não está disponível para a data selecionada.'})
        
        reserva = Reserva.objects.create(sala=sala, usuario=conta, data_reserva=data_reserva, hora_inicio=hora_inicio, hora_fim=hora_fim, preco_total=preco, multa=multas)
        return redirect("salas") 

    return render(request, "core/reservar.html", {"sala": sala , 'conta': conta})

def reservas(request):
    try:
        conta_id = request.session.get('usuario_id')
        conta = Usuario.objects.get(id=conta_id)

    except Usuario.DoesNotExist:
        conta = None
        return redirect('/')

    reservas = Reserva.objects.filter(usuario=conta)

    return render(request, "core/reservas.html", {'reservas': reservas, 'conta': conta})


def gerenciar_reserva(request, reserva_id):
    try:
        conta_id = request.session.get('usuario_id')
        conta = Usuario.objects.get(id=conta_id)

    except Usuario.DoesNotExist:
        conta = None
        return redirect('/')

    reserva = get_object_or_404(Reserva, id=reserva_id)

    if request.method == "POST" and request.POST.get("acao") == "multinha":
        valor = request.POST.get("valor")
        if valor:
            reserva.multa += decimal.Decimal(valor)
            reserva.preco_total += decimal.Decimal(valor)
            reserva.save()
            return redirect("reservas")
        else:
            return render(request, "core/gerenciar_reserva.html", {"reserva": reserva, 'conta': conta, 'error': 'Valor da multa é obrigatório.'})
    
    if request.method == "POST" and request.POST.get("acao") == "cancelar":
        
        
        return redirect("reservas")

    return render(request, "core/gerenciar_reserva.html", {"reserva": reserva, 'conta': conta})