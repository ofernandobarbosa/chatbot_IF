from rest_framework import viewsets
from app.models import Evento
from api.serializer import EventoSerializer, comprovante_de_matriculaSerializer, contato_dos_professoresSerializer, grade_de_horariosSerializer, calendario_academicoSerializer, informacoes_relevantes_dos_cursosSerializer, informacoes_sobre_inscricao_ou_matriculaSerializer, informacoes_sobre_rematriculaSerializer, requerimentos_ou_formulariosSerializer, tutoriais_de_acessos_a_sistemas_academicosSerializer
from app.views import categoria

class EventosViewSet(viewsets.ModelViewSet):
    """Todos Eventos"""
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    
class comprovante_de_matriculaViewSet(viewsets.ModelViewSet):
    """comprovante_de_matricula"""
    id = 10
    queryset = Evento.objects.all().filter(categoria=id)
    serializer_class = comprovante_de_matriculaSerializer

class contato_dos_professoresViewSet(viewsets.ModelViewSet):
    """contato_dos_professores"""
    id = 11
    queryset = Evento.objects.all().filter(categoria=id)
    serializer_class = contato_dos_professoresSerializer
    
class grade_de_horariosViewSet(viewsets.ModelViewSet):
    """grade_de_horarios"""
    id = 12
    queryset = Evento.objects.all().filter(categoria=id)
    serializer_class = grade_de_horariosSerializer
    
class calendario_academicoViewSet(viewsets.ModelViewSet):
    """calendario_academico"""
    id = 13
    queryset = Evento.objects.all().filter(categoria=id)
    serializer_class = calendario_academicoSerializer
    
class informacoes_relevantes_dos_cursosViewSet(viewsets.ModelViewSet):
    """informacoes_relevantes_dos_cursos"""
    id = 14
    queryset = Evento.objects.all().filter(categoria=id)
    serializer_class = informacoes_relevantes_dos_cursosSerializer
    
class informacoes_sobre_inscricao_ou_matriculaViewSet(viewsets.ModelViewSet):
    """informacoes_sobre_inscricao_ou_matricula"""
    id = 15
    queryset = Evento.objects.all().filter(categoria=id)
    serializer_class = informacoes_sobre_inscricao_ou_matriculaSerializer
    
class informacoes_sobre_rematriculaViewSet(viewsets.ModelViewSet):
    """informacoes_sobre_rematricula"""
    id = 16
    queryset = Evento.objects.all().filter(categoria=id)
    serializer_class = informacoes_sobre_rematriculaSerializer
    
class requerimentos_ou_formulariosViewSet(viewsets.ModelViewSet):
    """requerimentos_ou_formularios"""
    id = 17
    queryset = Evento.objects.all().filter(categoria=id)
    serializer_class = requerimentos_ou_formulariosSerializer
    
class tutoriais_de_acessos_a_sistemas_academicosViewSet(viewsets.ModelViewSet):
    """tutoriais_de_acessos_a_sistemas_academicos"""
    id = 18
    queryset = Evento.objects.all().filter(categoria=id)
    serializer_class = tutoriais_de_acessos_a_sistemas_academicosSerializer