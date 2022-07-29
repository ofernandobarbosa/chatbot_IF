from dataclasses import fields
from rest_framework import serializers
from app.models import Evento

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'
        
class comprovante_de_matriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['categoria','usuario','data_atualizacao', 'visivel', 'nome_evento','link_1','link_2','link_3']

class contato_dos_professoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['categoria','usuario','data_atualizacao', 'visivel', 'nome_do_professor','email','nome_da_disciplina']
        
class grade_de_horariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['categoria','usuario','data_atualizacao', 'visivel','modalidade_do_curso','nome_do_curso','ano','semestre','link_1']

class calendario_academicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['categoria','usuario','data_atualizacao', 'visivel','nome_evento','link_1','arquivo_1','ano']
        
class informacoes_relevantes_dos_cursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['categoria','usuario','data_atualizacao', 'visivel','modalidade_do_curso','nome_do_curso','descricao','forma_de_ingresso','requisitos','turno','numero_de_vagas','coordenador_do_curso','email_do_coordenador','email_do_curso']

class informacoes_sobre_inscricao_ou_matriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['categoria','usuario','data_atualizacao', 'visivel','nome_evento','descricao','link_1','link_2','link_3','arquivo_1','arquivo_2','arquivo_3']
        
class informacoes_sobre_rematriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['categoria','usuario','data_atualizacao', 'visivel','modalidade_do_curso','nome_do_curso','data_de_inicio','data_de_fim','link_1','link_2','link_3']

class requerimentos_ou_formulariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['categoria','usuario','data_atualizacao', 'visivel','nome_do_requerimento','descricao','data_de_inicio','data_de_fim','link_1','link_2','arquivo_1','arquivo_2','foto_1','foto_2']
        
class tutoriais_de_acessos_a_sistemas_academicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['categoria','usuario','data_atualizacao', 'visivel','nome_do_sistema','descricao','link_1','link_2','arquivo_1','arquivo_2']