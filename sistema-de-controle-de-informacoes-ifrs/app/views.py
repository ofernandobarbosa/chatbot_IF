from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Evento
from categorias.models import Categorias


def index(request):
    eventos = Evento.objects.filter(visivel=True)
    categorias = Categorias.objects.all()

    dados = {
        'eventos': eventos,
        'categorias': categorias,
    }

    return render(request, 'index.html', dados)

def evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    categorias = Categorias.objects.all()
    lista_models = ['categoria', 'usuario', 'nome_evento', 'descricao', 'nome_do_professor', 'nome_da_disciplina', 'email', 'email_do_coordenador', 'email_do_curso', 'modalidade_do_curso', 'nome_do_curso', 'ano', 'semestre', 'link_1', 'link_2', 'link_3', 'foto_1', 'foto_2', 'foto_3', 'arquivo_1', 'arquivo_2', 'arquivo_3', 'forma_de_ingresso', 'requisitos', 'turno', 'numero_de_vagas', 'coordenador_do_curso', 'nome_do_requerimento', 'nome_do_sistema', 'data_de_inicio', 'data_de_fim', 'data_atualizacao', 'visivel']
    
    evento_a_exibir = {
	    'evento' : evento,
        'categorias': categorias,
        'lista_models': lista_models,
    }
    
    return render(request,'evento.html', evento_a_exibir)

def categoria(request, categoria_id):
    
    categoria = get_object_or_404(Categorias, pk=categoria_id)
    eventos = Evento.objects.filter(visivel=True)
    categorias = Categorias.objects.all()
   
    categoria_a_exibir = {
	    'categoria' : categoria,
        'eventos': eventos,
        'categorias': categorias
    }
    
    return render(request,'categoria.html', categoria_a_exibir)

def buscar(request):    
    lista_eventos = Evento.objects.order_by('-data_atualizacao').filter(visivel=True)
    categorias = Categorias.objects.all()

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_1 = lista_eventos.filter(nome_evento__icontains=nome_a_buscar)
            lista_2 = lista_eventos.filter(nome_do_professor__icontains=nome_a_buscar)
            lista_3 = lista_eventos.filter(nome_do_curso__icontains=nome_a_buscar)
            lista_4 = lista_eventos.filter(nome_do_requerimento__icontains=nome_a_buscar)
            lista_5 = lista_eventos.filter(nome_do_sistema__icontains=nome_a_buscar)
            lista_6 = lista_eventos.filter(nome_da_disciplina__icontains=nome_a_buscar)
            lista_7 = lista_eventos.filter(descricao__icontains=nome_a_buscar)
            lista_8 = lista_eventos.filter(sobrenome_do_professor__icontains=nome_a_buscar)
            lista_9 = lista_eventos.filter(modalidade_de_ingresso__icontains=nome_a_buscar)
            lista_10 = lista_eventos.filter(coordenador_do_curso__icontains=nome_a_buscar)
    dados = {
	    'eventos1' : lista_1,
        'eventos2' : lista_2,
        'eventos3' : lista_3,
        'eventos4' : lista_4,
        'eventos5' : lista_5,
        'eventos6' : lista_6,
        'eventos7' : lista_7,
        'eventos8' : lista_8,
        'eventos9' : lista_9,
        'eventos10' : lista_10,             
        'categorias': categorias
    }
    return render(request, 'buscar.html', dados)