from django.db import models
from datetime import datetime
from categorias.models import Categorias
from django.contrib.auth.models import User

class Evento(models.Model):
    INGRESSO = (
        ('ENEM','ENEM'),
        ('Prova','Prova'),
        ('Pessoa Indígena','Pessoa Indígena'),
        ('Processo Seletivo EJA','Processo Seletivo EJA'),
        ('Sorteio','Sorteio'),
    )
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=254)
    nome_evento = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    nome_do_professor = models.CharField(max_length=254, blank=True)
    sobrenome_do_professor = models.CharField(max_length=254, blank=True)
    nome_da_disciplina = models.CharField(max_length=254, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    email_do_coordenador = models.EmailField(max_length=254, blank=True)
    email_do_curso = models.EmailField(max_length=254, blank=True)
    modalidade_do_curso = models.CharField(max_length=254, blank=True)
    modalidade_de_ingresso = models.CharField(max_length=100, choices=INGRESSO, blank=True)
    nome_do_curso = models.CharField(max_length=254, blank=True)
    ano = models.IntegerField(blank=True, null=True)
    semestre = models.IntegerField(blank=True, null=True)
    link_1 = models.CharField(max_length=254, blank=True)
    link_2 = models.CharField(max_length=254, blank=True)
    link_3 = models.CharField(max_length=254, blank=True)
    foto_1 = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    foto_2 = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    foto_3 = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)    
    arquivo_1 = models.FileField(upload_to='arquivo/%d/%m/%Y/', blank=True)
    arquivo_2 = models.FileField(upload_to='arquivo/%d/%m/%Y/', blank=True)
    arquivo_3 = models.FileField(upload_to='arquivo/%d/%m/%Y/', blank=True)
    forma_de_ingresso = models.CharField(max_length=254, blank=True)
    requisitos = models.CharField(max_length=254, blank=True)
    turno = models.CharField(max_length=50, blank=True)
    numero_de_vagas = models.IntegerField(blank=True, null=True)
    coordenador_do_curso = models.CharField(max_length=254, blank=True)
    nome_do_requerimento = models.CharField(max_length=254, blank=True)
    nome_do_sistema = models.CharField(max_length=254, blank=True)
    data_de_inicio = models.CharField(max_length=10, blank=True)
    data_de_fim = models.CharField(max_length=10, blank=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    visivel = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome_evento