from django.db import models

class Categorias(models.Model):
    CATEGORIA = (
        ('Comprovante de matrícula','Comprovante de matrícula'),
        ('Contato dos professores','Contato dos professores'),
        ('Grade de horários','Grade de horários'),
        ('Calendário acadêmico','Calendário acadêmico'),
        ('Informações relevantes dos cursos','Informações relevantes dos cursos'),
        ('Informações sobre inscrição/matrícula','Informações sobre inscrição/matrícula'),
        ('Informações sobre rematrícula','Informações sobre rematrícula'),
        ('Requerimentos/formulários','Requerimentos/formulários'),
        ('Tutoriais de acessos a sistemas acadêmicos','Tutoriais de acessos a sistemas acadêmicos'),
    )
    nome_categoria = models.CharField(max_length=100, choices=CATEGORIA)
    visivel = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome_categoria