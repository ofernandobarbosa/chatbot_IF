from django.db import models
from datetime import datetime

class Calendario(models.Model):
    
    CATEGORIA = (
        (1, 'Período Letivo'),
        (2, 'Feriados'),
        (3, 'Notícias'),
        (4, 'Processo Seletivo'),
        (5, 'Benefícios Estudantis'),
        (6, 'Cursos Ofertados'),
        (7, 'EAD'),
        (8, 'Informações de Servidores'),
        (9, 'Informações do IFRS'),
    )
    
    nome_evento = models.CharField(max_length=100)
    informacoes_evento = models.TextField()
    data_evento = models.DateField(auto_now=False, blank=True)
    imagem_evento = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    categoria_evento = models.IntegerField(choices=CATEGORIA)
    data_atualizacao = models.DateTimeField(default=datetime.now, blank=True)
    visivel = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome_evento
    
class Categoria(models.Model):
        
    nome_categoria = models.CharField(max_length=100)
    visivel = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome_categoria    
    