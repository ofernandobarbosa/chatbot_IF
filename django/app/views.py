from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Calendario
from .models import Categoria


def index(request):
    calendarios = Calendario.objects.filter(visivel=True)
    categorias = Categoria.objects.all()

    dados = {
        'calendarios': calendarios,
        'categorias': categorias
    }

    return render(request, 'index.html', dados)

def calendario(request, calendario_id):
    calendario = get_object_or_404(Calendario, pk=calendario_id)
    categorias = Categoria.objects.all()
    
    calendario_a_exibir = {
	    'calendario' : calendario,
        'categorias': categorias
    }
    
    return render(request,'calendario.html', calendario_a_exibir)

def categoria(request, categoria_id):
    
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    calendarios = Calendario.objects.filter(visivel=True)
    categorias = Categoria.objects.all()
   
    categoria_a_exibir = {
	    'categoria' : categoria,
        'calendarios': calendarios,
        'categorias': categorias
    }
    
    return render(request,'categoria.html', categoria_a_exibir)

def buscar(request):    
    lista_eventos = Calendario.objects.order_by('-data_atualizacao').filter(visivel=True)
    categorias = Categoria.objects.all()

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_eventos = lista_eventos.filter(nome_evento__icontains=nome_a_buscar)

    dados = {
	    'calendarios' : lista_eventos,
        'categorias': categorias
    }
    return render(request, 'buscar.html', dados)