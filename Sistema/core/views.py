from django.shortcuts import render , redirect
from .models import Registro
from django.contrib import messages

# Uma view é um “tipo” de página em sua aplicação Django que em geral serve uma função específica
#  e tem um template específico. 
# Por exemplo, em nossa aplicação, você deve ter as seguintes views:
# Create your views here.

def home(request):# função que retorna a pagina inicial
    registros=Registro.objects.all()
    return render(request, 'index.html',{'registro':registros})

def registrarHoras(request):# função que retorna a pagina de registro de horas
    codigo = request.POST['txtCodigo']
    nome = request.POST['txtNome']
    horas = request.POST['numHoras']

    registros = Registro.objects.create(codigo=codigo, nome=nome, horas=horas)
    messages.success(request, 'Horas Registradas')
    return redirect('/')


def edicaoHoras(request, codigo):# função que retorna a pagina de edição de horas
    registros = Registro.objects.get(codigo=codigo)
    return render(request, "edicaoHoras.html", {"registros": registros})


def editarHoras(request):# função que retorna a pagina de edição de horas
    codigo = request.POST['txtCodigo']
    nome = request.POST['txtNome']
    horas = request.POST['numHoras']

    registros = Registro.objects.get(codigo=codigo)
    registros.nome = nome
    registros.horas = horas

    registros.save()
    messages.success(request, 'Registro atualizado')
    return redirect('/')

def deletarHoras(request, codigo):# função que retorna a pagina de edição de horas
    registros = Registro.objects.get(codigo=codigo)
    registros.delete()

    messages.success(request, 'Registro  Deletado')

    return redirect('/')
