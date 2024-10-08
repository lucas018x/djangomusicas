from django.shortcuts import redirect, render, get_object_or_404
from .models import Estilos

def listar_estilos(request):
    estilos = Estilos.objects.all()
    return render(request, 'listarestilo.html', {'estilos':estilos})

def cadastrar_estilos(request):
  if request.method == 'POST':
        nome = request.POST ['nome']
        sigla = request.POST ['sigla']
        Estilos.objects.create(nome=nome, sigla=sigla)
        return redirect('listar_estilo')
  return render (request,'formestilo.html')

def editar_estilos(request, id):
    estilo = get_object_or_404(Estilos,id = id)
    if request.method == "POST":
        estilo.nome = request.POST['nome']
        estilo.sigla = request.POST['sigla']
        estilo.save()
        return redirect('lista_estilo')
    return render(request, 'formestilo.html', {'estilo' : estilo})

def excluir_estilos(request, id):
    estilo = get_object_or_404(Estilos, id=id)
    if request.method == "POST":
        estilo.delete()
        return redirect('listar_estilo')
    return render(request, 'confirmar_exclusao.html', {'estilo' : estilo})
