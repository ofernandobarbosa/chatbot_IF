from rest_framework import generics
from django.shortcuts import render

try:
    
    from app.models import Evento
    from categorias.models import Categorias
    from api.serializer import Eventos_todosSerializer, comprovante_de_matriculaSerializer, contato_dos_professoresSerializer, grade_de_horariosSerializer, calendario_academicoSerializer, informacoes_relevantes_dos_cursosSerializer, informacoes_sobre_inscricao_ou_matriculaSerializer, informacoes_sobre_rematriculaSerializer, requerimentos_ou_formulariosSerializer, tutoriais_de_acessos_a_sistemas_academicosSerializer
    from app.views import categoria
except:
    None
    
try:
    def api(request):
        categorias = Categorias.objects.all()
        dados = {
            'categorias': categorias,
        }
        return render(request, 'api.html', dados)
except:
    def api(request):
        pass
    
try:
    class Eventos_todos(generics.ListAPIView):
        queryset = Evento.objects.all()
        serializer_class = Eventos_todosSerializer
except:
    class Eventos_todos(generics.ListAPIView):
        pass
        
try:        
    class comprovante_de_matricula(generics.ListAPIView):
        """comprovante_de_matricula"""
        cat = Categorias.objects.all()
        global id
        for c in cat:
            if c.nome_categoria == "Comprovante de matrícula":
                id = c.id
        queryset = Evento.objects.all().order_by('-data_atualizacao').filter(categoria=id).filter(visivel=True)
        serializer_class = comprovante_de_matriculaSerializer
except:
    class comprovante_de_matricula(generics.ListAPIView):
        pass

try:
    class contato_dos_professores(generics.ListAPIView):
        """contato_dos_professores"""
        cat = Categorias.objects.all()
        global id
        for c in cat:
            if c.nome_categoria == "Contato dos professores":
                id = c.id
        queryset = Evento.objects.all().order_by('-data_atualizacao').filter(categoria=id).filter(visivel=True)
        serializer_class = contato_dos_professoresSerializer
except:
    class contato_dos_professores(generics.ListAPIView):
        pass
    
try:        
    class grade_de_horarios(generics.ListAPIView):
        """grade_de_horarios"""
        cat = Categorias.objects.all()
        global id
        for c in cat:
            if c.nome_categoria == "Grade de horários":
                id = c.id
        queryset = Evento.objects.all().order_by('-data_atualizacao').filter(categoria=id).filter(visivel=True)
        serializer_class = grade_de_horariosSerializer
except:
    class grade_de_horarios(generics.ListAPIView):
        pass

try:        
    class calendario_academico(generics.ListAPIView):
        """calendario_academico"""
        cat = Categorias.objects.all()
        global id
        for c in cat:
            if c.nome_categoria == "Calendário acadêmico":
                id = c.id
        queryset = Evento.objects.all().order_by('-data_atualizacao').filter(categoria=id).filter(visivel=True)
        serializer_class = calendario_academicoSerializer
except:
    class calendario_academico(generics.ListAPIView):
        pass

try:        
    class informacoes_relevantes_dos_cursos(generics.ListAPIView):
        """informacoes_relevantes_dos_cursos"""
        cat = Categorias.objects.all()
        global id
        for c in cat:
            if c.nome_categoria == "Informações relevantes dos cursos":
                id = c.id
        queryset = Evento.objects.all().order_by('-data_atualizacao').filter(categoria=id).filter(visivel=True)
        serializer_class = informacoes_relevantes_dos_cursosSerializer
except:
    class informacoes_relevantes_dos_cursos(generics.ListAPIView):
        pass

try:        
    class informacoes_sobre_inscricao_ou_matricula(generics.ListAPIView):
        """informacoes_sobre_inscricao_ou_matricula"""
        cat = Categorias.objects.all()
        global id
        for c in cat:
            if c.nome_categoria == "Informações sobre inscrição/matrícula":
                id = c.id
        queryset = Evento.objects.all().order_by('-data_atualizacao').filter(categoria=id).filter(visivel=True)
        serializer_class = informacoes_sobre_inscricao_ou_matriculaSerializer
except:
    class informacoes_sobre_inscricao_ou_matricula(generics.ListAPIView):
        pass

try:        
    class informacoes_sobre_rematricula(generics.ListAPIView):
        """informacoes_sobre_rematricula"""
        cat = Categorias.objects.all()
        global id
        for c in cat:
            if c.nome_categoria == "Informações sobre rematrícula":
                id = c.id
        queryset = Evento.objects.all().order_by('-data_atualizacao').filter(categoria=id).filter(visivel=True)
        serializer_class = informacoes_sobre_rematriculaSerializer
except:
    class informacoes_sobre_rematricula(generics.ListAPIView):
        pass

try:        
    class requerimentos_ou_formularios(generics.ListAPIView):
        """requerimentos_ou_formularios"""
        cat = Categorias.objects.all()
        global id
        for c in cat:
            if c.nome_categoria == "Requerimentos/formulários":
                id = c.id
        queryset = Evento.objects.all().order_by('-data_atualizacao').filter(categoria=id).filter(visivel=True)
        serializer_class = requerimentos_ou_formulariosSerializer
except:
    class requerimentos_ou_formularios(generics.ListAPIView):
        pass

try:        
    class tutoriais_de_acessos_a_sistemas_academicos(generics.ListAPIView):
        """tutoriais_de_acessos_a_sistemas_academicos"""
        cat = Categorias.objects.all()
        global id
        for c in cat:
            if c.nome_categoria == "Tutoriais de acessos a sistemas acadêmicos":
                id = c.id
        queryset = Evento.objects.all().order_by('-data_atualizacao').filter(categoria=id).filter(visivel=True)
        serializer_class = tutoriais_de_acessos_a_sistemas_academicosSerializer
except:
    class tutoriais_de_acessos_a_sistemas_academicos(generics.ListAPIView):
        pass