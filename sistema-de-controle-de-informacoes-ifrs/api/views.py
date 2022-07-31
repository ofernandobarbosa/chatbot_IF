from rest_framework import viewsets
from app.models import Evento
from categorias.models import Categorias
from api.serializer import EventoSerializer, comprovante_de_matriculaSerializer, contato_dos_professoresSerializer, grade_de_horariosSerializer, calendario_academicoSerializer, informacoes_relevantes_dos_cursosSerializer, informacoes_sobre_inscricao_ou_matriculaSerializer, informacoes_sobre_rematriculaSerializer, requerimentos_ou_formulariosSerializer, tutoriais_de_acessos_a_sistemas_academicosSerializer
from app.views import categoria

class EventosViewSet(viewsets.ModelViewSet):
    """Todos Eventos"""
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    
class comprovante_de_matriculaViewSet(viewsets.ModelViewSet):
    """comprovante_de_matricula"""
    cat = Categorias.objects.all()
    global id
    for c in cat:
        if c.nome_categoria == "Comprovante de matrícula":
            id = c.id
    queryset = Evento.objects.all().order_by('-data_atualizacao').filter(categoria=id).filter(visivel=True)
    serializer_class = comprovante_de_matriculaSerializer

class contato_dos_professoresViewSet(viewsets.ModelViewSet):
    """contato_dos_professores"""
    cat = Categorias.objects.all()
    global id
    for c in cat:
        if c.nome_categoria == "Contato dos professores":
            id = c.id
    queryset = Evento.objects.all().order_by('-data_atualizacao').filter(categoria=id).filter(visivel=True)
    serializer_class = contato_dos_professoresSerializer
    
class grade_de_horariosViewSet(viewsets.ModelViewSet):
    """grade_de_horarios"""
    cat = Categorias.objects.all()
    global id
    for c in cat:
        if c.nome_categoria == "Grade de horários":
            id = c.id
    queryset = Evento.objects.all().order_by('-data_atualizacao').filter(categoria=id).filter(visivel=True)
    serializer_class = grade_de_horariosSerializer
    
class calendario_academicoViewSet(viewsets.ModelViewSet):
    """calendario_academico"""
    cat = Categorias.objects.all()
    global id
    for c in cat:
        if c.nome_categoria == "Calendário acadêmico":
            id = c.id
    queryset = Evento.objects.all().order_by('-data_atualizacao').filter(categoria=id).filter(visivel=True)
    serializer_class = calendario_academicoSerializer
    
class informacoes_relevantes_dos_cursosViewSet(viewsets.ModelViewSet):
    """informacoes_relevantes_dos_cursos"""
    cat = Categorias.objects.all()
    global id
    for c in cat:
        if c.nome_categoria == "Informações relevantes dos cursos":
            id = c.id
    queryset = Evento.objects.all().order_by('-data_atualizacao').filter(categoria=id).filter(visivel=True)
    serializer_class = informacoes_relevantes_dos_cursosSerializer
    
class informacoes_sobre_inscricao_ou_matriculaViewSet(viewsets.ModelViewSet):
    """informacoes_sobre_inscricao_ou_matricula"""
    cat = Categorias.objects.all()
    global id
    for c in cat:
        if c.nome_categoria == "Informações sobre inscrição/matrícula":
            id = c.id
    queryset = Evento.objects.all().order_by('-data_atualizacao').filter(categoria=id).filter(visivel=True)
    serializer_class = informacoes_sobre_inscricao_ou_matriculaSerializer
    
class informacoes_sobre_rematriculaViewSet(viewsets.ModelViewSet):
    """informacoes_sobre_rematricula"""
    cat = Categorias.objects.all()
    global id
    for c in cat:
        if c.nome_categoria == "Informações sobre rematrícula":
            id = c.id
    queryset = Evento.objects.all().order_by('-data_atualizacao').filter(categoria=id).filter(visivel=True)
    serializer_class = informacoes_sobre_rematriculaSerializer
    
class requerimentos_ou_formulariosViewSet(viewsets.ModelViewSet):
    """requerimentos_ou_formularios"""
    cat = Categorias.objects.all()
    global id
    for c in cat:
        if c.nome_categoria == "Requerimentos/formulários":
            id = c.id
    queryset = Evento.objects.all().order_by('-data_atualizacao').filter(categoria=id).filter(visivel=True)
    serializer_class = requerimentos_ou_formulariosSerializer
    
class tutoriais_de_acessos_a_sistemas_academicosViewSet(viewsets.ModelViewSet):
    """tutoriais_de_acessos_a_sistemas_academicos"""
    cat = Categorias.objects.all()
    global id
    for c in cat:
        if c.nome_categoria == "Tutoriais de acessos a sistemas acadêmicos":
            id = c.id
    queryset = Evento.objects.all().order_by('-data_atualizacao').filter(categoria=id).filter(visivel=True)
    serializer_class = tutoriais_de_acessos_a_sistemas_academicosSerializer
