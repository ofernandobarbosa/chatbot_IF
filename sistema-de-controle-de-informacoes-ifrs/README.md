# DA INSTALAÇÃO
------------

## Da Máquina Virtual
### Devemos instalar o ambiente virtual VENV no Windows, Linux ou macOS para não ter problemas com versões do Python e do Django:

### Criamos uma pasta para aplicação, chamamos essa pasta de “Sistema de Controle de Informações” (mas poderia ser qualquer nome).

### dentro dessa pasta que acabamos de criar, digitando ```cd  Sistema de Controle de Informações```, digitaremos o comando:

```

python3 -m venv ./venv

```

### Neste caso, estamos instalando o ambiente virtual na pasta atual '.' e colocando os arquivos da instalação na subpasta 'venv'.

### Após este comando, digite 'code .' para abrir a pasta inteira no Visual Studio Code e, no terminal do Visual Studio, caso esteja utilizando Linuxo ou macOS digite:
```
source venv/bin/activate
```
Ou então, caso esteja utilizando Windows:
```
venv\Scripts\activate.bat
```


### Dessa forma aparecerá a expressão 'venv' no terminal, demonstrando estar executando o ambiente virtual escolhido.

------------

## Do Django
### No ambiente virtual, em seguida, instalamos o Django através do comando:
```
pip install Django
```
### Neste caso, instalamos a última versão do Framework Django naquele momento, Versão 4.1, dentro da pasta “Sistema de Controle de Informações”.

### Em seguida, com o Django instalado, iniciamos nosso projeto Django, através do comando:
```
django-admin startproject principal .
```
### Destaque-se que denominamos nossa aplicação como “principal”, na pasta ‘raiz’, foi criado um arquivo denominado ‘manage.py’ que é responsável por administrar as principais funções do Django,  já na pasta denominada principal foram criados diversos arquivos, dentre eles o urls.py, o settings.py que são responsáveis pelas rotas e pelas configurações da aplicação respectivamente.

------------

## Dos APPs
### Criamos, ao todo, 4 aplicações para facilitar a escrita e, também, a divisão de funções de nossa aplicação principal, foram elas denominadas: api, app, categorias e usuários.

### api
``` python manage.py startapp api```
#### Aplicação responsável pela administração dos Endpoints de nossa aplicação.

### app
``` python manage.py startapp app```
#### Aplicação responsável pelo model Evento, pela exibição das informações cadastradas na aplicação e, também, pela página de busca.
### categorias
``` python manage.py startapp categorias```
#### Aplicação responsável por gerenciar as categorias cadastradas e vinculá-la, via chave estrangeira, ao model Evento.
### usuarios
``` python manage.py startapp usuarios```
#### Aplicação responsável pela gestão de usuários e, também, cadastro, por parte destes, de eventos no banco de dados, em geral, a criação de dados no Banco se dará através desta aplicação. 
 
# DOS MODELS
### App app, arquivo models.py
```py
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
```

### App categorias, arquivo models.py
```py
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
```

 
# DAS VIEWS
 

# DOS TEMPLATES
## Dos Arquivos HTML
### Dos Elementos Python no HTML
### Repartindo arquivos

## Dos Arquivos Estáticos
 

# DOS URLS
## App Api
```py
from django.urls import path
from . import views
urlpatterns = [
  	path('', views.api, name='api'),
]
```
## App App
```py
from django.urls import path
from . import views
urlpatterns = [
	path('', views.index, name='index'),
 	path('evento/<int:evento_id>' , views.evento, name='evento'),
  	path('categoria/<int:categoria_id>', views.categoria, name='categoria'),
   	path('buscar', views.buscar, name = 'buscar'),
]
```
## App Categorias
```py
from django.urls import path
from . import views
urlpatterns = [
	path('categorias', views.categorias, name='categorias'),
]
```
## App Usuarios
```py
from django.urls import path
from . import views
urlpatterns = [
	path('cadastro', views.cadastro, name='cadastro'), 
    path('add_evento/<int:categorias_id>', views.add_evento, name='add_evento'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('cria_evento', views.cria_evento, name='cria_evento'),
    path('formulario', views.formulario, name='formulario'),
]
```
## App Principal
```py
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
try:
    from api.views import Eventos_todos, comprovante_de_matricula, contato_dos_professores, grade_de_horarios, calendario_academico, informacoes_relevantes_dos_cursos, informacoes_sobre_inscricao_ou_matricula, informacoes_sobre_rematricula, requerimentos_ou_formularios, tutoriais_de_acessos_a_sistemas_academicos
except:
    None
urlpatterns = [
    path('', include('app.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('categorias/', include('categorias.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),        
    path('api/eventos', Eventos_todos.as_view()),
    path('api/comprovante_de_matricula', comprovante_de_matricula.as_view()),
    path('api/contato_dos_professores', contato_dos_professores.as_view()),
    path('api/grade_de_horarios', grade_de_horarios.as_view()),
    path('api/calendario_academico', calendario_academico.as_view()),
    path('api/informacoes_relevantes_dos_cursos', informacoes_relevantes_dos_cursos.as_view()),
    path('api/informacoes_sobre_inscricao_ou_matricula', informacoes_sobre_inscricao_ou_matricula.as_view()),
    path('api/informacoes_sobre_rematricula', informacoes_sobre_rematricula.as_view()),
    path('api/requerimentos_ou_formularios', requerimentos_ou_formularios.as_view()),
    path('api/tutoriais_de_acessos_a_sistemas_academicos', tutoriais_de_acessos_a_sistemas_academicos.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
```


 

# DO BANCO DE DADOS
## Da Instalação do Postgresql
### Optamos por utilizar o Postgresql por sua fácil comunicação com o Django, e porque nossa aplicação não necessitava de banco de dados não relacional. Após a instalação do Postgres que pode ser feita de diferentes formas em diferentes plataformas, passamos à instalação dos módulos em nossa aplicação via ‘pip’.

### Além disso, instalamos o módulo de comunicação do Django com este banco de dados, o psycopg2 e seus binários através do psycopg2-binary, ou seja, instalamos via pip da seguinte forma:
``` pip install psycopg2 ```

### E também:

``` pip install psycopg2-binary ```

## Da Configuração do Banco de Dados

### Configuramos o arquivo ‘settings.py’, na variável DATABASES, da seguinte forma:

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': ‘#######’,
        'USER': ‘#######’,
        'PASSWORD': ‘#######’,
        'HOST':'localhost'
    }
}
```

## Da Criação de Dados no Banco de Dados

### Após a instalação e configuração do Postgresql em nossa aplicação Django, criamos um servidor chamado #######, com usuário chamado #######, senha ####### e endereço, inicialmente, localhost para configuração local.


 
# DOS USUÁRIOS E DO LOGIN
## Do Usuário Admin
## Dos Demais Usuários

 
# DA INTERFACE E UTILIZAÇÃO
 
# DOS ENDPOINTS
## Página Principal Com Lista dos Endpoints:
### http://localhost:8000/api/
## Endpoints de Todos Eventos
```
GET /api/eventos
EXEMPLO:

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "usuario": "Anderson", 
        "nome_evento": "Comprovante de Matrícula TADS",
        "descricao": "",
        "nome_do_professor": "",
        "sobrenome_do_professor": "",
        "nome_da_disciplina": "",
        "email": "",
        "email_do_coordenador": "",
        "email_do_curso": "",
        "modalidade_do_curso": "",
        "modalidade_de_ingresso": "",
        "nome_do_curso": "",
        "ano": null,
        "semestre": null,
        "link_1": "www.comprovantedematriculatads.com.br",
        "link_2": "",
        "link_3": "",
        "foto_1": null,
        "foto_2": null,
        "foto_3": null,
        "arquivo_1": null,
        "arquivo_2": null,
        "arquivo_3": null,
        "forma_de_ingresso": "",
        "requisitos": "",
        "turno": "",
        "numero_de_vagas": null,
        "coordenador_do_curso": "",
        "nome_do_requerimento": "",
        "nome_do_sistema": "",
        "data_de_inicio": "",
        "data_de_fim": "",
        "data_atualizacao": "2022-08-04T18:00:51.243909-03:00",
        "visivel": true,
        "categoria": 1
    },
[...]
    {
        "id": 10,
        "usuario": "Anderson",
        "nome_evento": "",
        "descricao": "Aqui você recebe informações sobre o sistema SIGAA de forma detalhada",
        "nome_do_professor": "",
        "sobrenome_do_professor": "",
        "nome_da_disciplina": "",
        "email": "",
        "email_do_coordenador": "",
        "email_do_curso": "",
        "modalidade_do_curso": "",
        "modalidade_de_ingresso": "",
        "nome_do_curso": "",
        "ano": null,
        "semestre": null,
        "link_1": "www.sigaaaaaa.orkut.com.br",
        "link_2": "",
        "link_3": "",
        "foto_1": null,
        "foto_2": null,
        "foto_3": null,
        "arquivo_1": null,
        "arquivo_2": null,
        "arquivo_3": null,
        "forma_de_ingresso": "",
        "requisitos": "",
        "turno": "",
        "numero_de_vagas": null,
        "coordenador_do_curso": "",
        "nome_do_requerimento": "",
        "nome_do_sistema": "Sigaa",
        "data_de_inicio": "",
        "data_de_fim": "",
        "data_atualizacao": "2022-08-05T00:58:21.839630-03:00",
        "visivel": true,
        "categoria": 9
    }
]
```
## Endpoints de Comprovante De Matricula
```
GET /api/comprovante_de_matricula

EXEMPLO:

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "categoria": 1,
        "usuario": "Anderson",
        "data_atualizacao": "2022-08-04T18:00:51.243909-03:00",
        "visivel": true,
        "nome_evento": "Comprovante de Matrícula TADS",
        "link_1": "www.comprovantedematriculatads.com.br",
        "link_2": "",
        "link_3": ""
    }
]
```
## Endpoints de Contato Dos Professores
```
GET /api/contato_dos_professores

EXEMPLO:

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 2,
        "categoria": 2,
        "usuario": "Anderson",
        "data_atualizacao": "2022-08-04T18:15:06.636962-03:00",
        "visivel": true,
        "nome_do_professor": "Fulano",
        "sobrenome_do_professor": "De Tal",
        "email": "fulano@ifrs.com.br",
        "nome_da_disciplina": "Fulanice"
    }
]

```
## Endpoints de Grade De Horarios
```
GET /api/grade_de_horarios

EXEMPLO:

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 4,
        "categoria": 3,
        "usuario": "Anderson",
        "data_atualizacao": "2022-08-05T00:50:26.900924-03:00",
        "visivel": true,
        "modalidade_do_curso": "Superior",
        "nome_do_curso": "Tads",
        "ano": 2022,
        "semestre": 2,
        "link_1": "www.gradedehorariotads.com.br"
    }
]
```
## Endpoints de Calendario Academico
```
GET /api/calendario_academico

EXEMPLO:

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 5,
        "categoria": 4,
        "usuario": "Anderson",
        "data_atualizacao": "2022-08-05T00:51:06.532128-03:00",
        "visivel": true,
        "nome_evento": "Calendário Acadêmico Julho 2022",
        "link_1": "www.calendarioacademicodejulhode2022.com.br",
        "arquivo_1": "http://localhost:8000/media/arquivo/05/08/2022/calendario-julho.png",
        "ano": 2022
    }
]
```
## Endpoints de Informacoes Relevantes Dos Cursos
```
GET /api/informacoes_relevantes_dos_cursos

EXEMPLO:

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 6,
        "categoria": 5,
        "usuario": "Anderson",
        "data_atualizacao": "2022-08-05T00:53:55.701548-03:00",
        "visivel": true,
        "modalidade_do_curso": "Superior",
        "nome_do_curso": "Tads",
        "descricao": "Essa é uma descrição muito pouco detalhada, mas que poderia ser bem mais detalhada caso houvesse informações no momento em que foi escrita sobre o curso de Tecnólogo em Análise e Desenvolvimento de Sistemas do IFRS, poderia conter a carga horária e a grade curricular, por exemplo",
        "forma_de_ingresso": "ENEM",
        "requisitos": "Aqui poderiam ser listados alguns requisitos para o ingresso no curso do evento, por exemplo, que é exigido ensino médio completo, certificado de reservista, quitação eleitoral e etc.",
        "turno": "Noturno",
        "numero_de_vagas": 30,
        "coordenador_do_curso": "Luciano",
        "email_do_coordenador": "luciano@ifrs.com.br",
        "email_do_curso": "tads.ifrs@ifrs.com.br"
    }
]
```
## Endpoints de Informacoes Sobre Inscricao Ou Matricula
```
GET /api/informacoes_sobre_inscricao_ou_matricula

EXEMPLO:

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 7,
        "categoria": 6,
        "usuario": "Anderson",
        "data_atualizacao": "2022-08-05T00:55:18.752574-03:00",
        "visivel": true,
        "modalidade_de_ingresso": "ENEM",
        "nome_evento": "Matrícula No Curso Tads",
        "descricao": "Aqui segue a descrição das informações necessárias para realizar a matrícula junto ao curso TADS no Ifrs.",
        "link_1": "www.linksobreamatriculanotads.com.br",
        "link_2": "",
        "link_3": "",
        "arquivo_1": null,
        "arquivo_2": null,
        "arquivo_3": null
    }
]
```
## Endpoints de Informacoes Sobre Rematricula
```
GET /api/informacoes_sobre_rematricula

EXEMPLO:

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 8,
        "categoria": 7,
        "usuario": "Anderson",
        "data_atualizacao": "2022-08-05T00:55:49.229793-03:00",
        "visivel": true,
        "modalidade_do_curso": "Superior",
        "nome_do_curso": "Tads",
        "data_de_inicio": "01/01/2023",
        "data_de_fim": "15/01/2023",
        "link_1": "www.rematriculadotads.com.br",
        "link_2": "",
        "link_3": ""
    }
]
```
## Endpoints de Requerimentos Ou Formularios
```
GET /api/requerimentos_ou_formularios

EXEMPLO:

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 9,
        "categoria": 8,
        "usuario": "Anderson",
        "data_atualizacao": "2022-08-05T00:57:38.311161-03:00",
        "visivel": true,
        "nome_do_requerimento": "Atividades Complementares",
        "descricao": "Aqui você recebe informações sobre como fazer o requerimento para solicitar inclusão de atividades complementares.",
        "data_de_inicio": "01/10/2022",
        "data_de_fim": "01/01/2023",
        "link_1": "www.requerimentodeatividadecomplementar.com.br",
        "link_2": ""
    }
]
```
## Endpoints de Tutoriais De Acessos A Sistemas Academicos
```
GET /api/tutoriais_de_acessos_a_sistemas_academicos

EXEMPLO:

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 10,
        "categoria": 9,
        "usuario": "Anderson",
        "data_atualizacao": "2022-08-05T00:58:21.839630-03:00",
        "visivel": true,
        "nome_do_sistema": "Sigaa",
        "descricao": "Aqui você recebe informações sobre o sistema SIGAA de forma detalhada",
        "link_1": "www.sigaaaaaa.orkut.com.br",
        "link_2": ""
    }
]
```



 
# RECURSOS UTILIZADOS
## Requirements.txt
```
asgiref==3.5.2
Django==4.1
django-filter==22.1
djangorestframework==3.13.1
Markdown==3.4.1
Pillow==9.2.0
psycopg2==2.9.3
psycopg2-binary==2.9.3
pytz==2022.1
sqlparse==0.4.2
tzdata==2022.1
```
## Da Instalação Destes Pacotes
```
pip install Django
pip install django-filter
pip install djangorestframework
pip install Markdown
pip install Pillow
pip install psycopg2
pip install psycopg2-binary
```
### Dos Demais Recursos Utilizados
- [Visual Studio Code](https://code.visualstudio.com/)

- [Venv](https://docs.python.org/3/library/venv.html)

- [Python](https://www.python.org/)

- [Bootstrap](https://getbootstrap.com/)

- [PgAdmin / Postgresql](https://www.pgadmin.org/)
 
# DO TRABALHO
## SOBRE O PROJETO

## SOBRE O GRUPO
### INTEGRANTES

