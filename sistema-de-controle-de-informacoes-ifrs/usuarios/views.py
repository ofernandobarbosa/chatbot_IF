from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from categorias.models import Categorias
from app.models import Evento
from django.contrib.auth.models import User
from django.contrib import auth

def cadastro(request):
    categorias = Categorias.objects.all()
    dados = {
        'categorias': categorias
    }

    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            print('O campo e-mail não pode ficar em branco')
            return redirect('cadastro')
        if not password.strip():
            print('O campo senha não pode ficar em branco')
            return redirect('cadastro')
        if not password2.strip():
            print('O campo confirmação da senha não pode ficar em branco')
            return redirect('cadastro')
        if password != password2:
            print('As senhas digitadas não conferem')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')
        nome = nome.title()
        user = User.objects.create_user(
            username=nome, email=email, password=password)
        user.save()
        print('Usuário criado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html', dados)

def login(request):
    categorias = Categorias.objects.all()
    dados = {
        'categorias': categorias
    }
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email == "" or password == "":
            print('os campos email e senha não podem ficar em branco')
            return redirect('login')
        elif User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list(
                'username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=password)
            if user is not None:
                auth.login(request, user)
                print('login realizado com sucesso')
                return redirect('dashboard')
            else:
                print('Não foi possível realizar este login')
                return redirect('login')
        else:
            print('Email não localizado')
            return redirect('login')
    else:
        return render(request, 'usuarios/login.html', dados)

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    categorias = Categorias.objects.all()
    eventos = Evento.objects.order_by('-data_atualizacao').filter(visivel=True)
    dados = {
        'categorias': categorias,
        'eventos': eventos
    }

    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def cria_evento(request):
    global categoria_selecionada
    categorias = Categorias.objects.all()
    dados = {
        'categorias': categorias
    }
    if request.method == 'POST':
        categoria_selecionada = request.POST['selecionado']
        print (categoria_selecionada)
        return redirect('add_evento')
    else:
        return render(request, 'usuarios/cria_evento.html', dados)

def add_evento(request, categorias_id):
    categorias = Categorias.objects.all()
    evento = Evento.objects.all()
    categoria = get_object_or_404(Categorias, pk=categorias_id)
    dados = {
        'categoria': categoria,
        'categorias': categorias,
        'evento': evento,
    }
    return render(request, 'usuarios/add_evento.html', dados)

def formulario(request):
    categorias = Categorias.objects.all()
    global id    
    if request.method == 'POST':        
        categoria = request.POST['categoria']
        for cat in categorias:
            if categoria == cat.nome_categoria:
                id = cat.id
        # CONTATO DOS PROFESSORES - BANCO DE DADOS
        if categoria == "Contato dos professores":
            usuario = request.POST['usuario']
            nome_do_professor = request.POST['nome_do_professor']
            email = request.POST['email']
            nome_da_disciplina = request.POST['nome_da_disciplina']
            try:
                visivel = request.POST['visivel']
                visivel = True
            except:
                visivel = False
            if not nome_do_professor.strip():
                print('O campo nome do professor não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not email.strip():
                print('O campo email não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not nome_da_disciplina.strip():
                print('O campo nome da disciplina não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            nome_do_professor = nome_do_professor.title()
            try:
                evento = Evento.objects.create(categoria=Categorias.objects.get(pk=id), usuario=usuario, nome_do_professor=nome_do_professor, email=email, nome_da_disciplina=nome_da_disciplina, visivel=visivel)
                evento.save()
                print("Contato do Professor Cadastrado com Sucesso")
                return render(request, 'usuarios/cadastrado_com_sucesso.html')
            except:
                print("Não foi possível incluir no banco de dados")
                return render(request, 'usuarios/nao_foi_cadastrado.html')
        
        # COMPROVANTE DE MATRÍCULA - BANCO DE DADOS
        elif categoria == "Comprovante de matrícula":
            usuario = request.POST['usuario']
            nome_evento = request.POST['nome_evento']
            link_1 = request.POST['link_1']
            try:
                link_2 = request.POST['link_2']
            except:
                link_2 = ""
            try:
                link_3 = request.POST['link_3']
            except:
                link_3 = ""
            try:
                visivel = request.POST['visivel']
                visivel = True
            except:
                visivel = False
            if not nome_evento.strip():
                print('O campo nome evento não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not link_1.strip():
                print('O campo link 1 não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            try:
                evento = Evento.objects.create(categoria=Categorias.objects.get(pk=id), usuario=usuario, nome_evento=nome_evento, link_1=link_1, link_2=link_2, link_3=link_3, visivel=visivel)
                evento.save()
                print("Comprovante de Matrícula Cadastrado com Sucesso")
                return render(request, 'usuarios/cadastrado_com_sucesso.html')
            except:
                print("Não foi possível incluir no banco de dados")
                return render(request, 'usuarios/nao_foi_cadastrado.html')
            
        # GRADE DE HORÁRIOS - BANCO DE DADOS
        elif categoria == "Grade de horários":
            usuario = request.POST['usuario']
            try:
                visivel = request.POST['visivel']
                visivel = True
            except:
                visivel = False
            modalidade_do_curso = request.POST['modalidade_do_curso']
            nome_do_curso = request.POST['nome_do_curso']
            ano = request.POST['ano']
            semestre = request.POST['semestre']
            link_1 = request.POST['link_1']
            if not modalidade_do_curso.strip():
                print('O campo modalidade do curso não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not nome_do_curso.strip():
                print('O campo nome do curso não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not ano.strip():
                print('O campo ano não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not semestre.strip():
                print('O campo semestre não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not link_1.strip():
                print('O campo link 1 não pode ficar em branco')
                return redirect('nao_foi_cadastrado')            
            try:
                evento = Evento.objects.create(categoria=Categorias.objects.get(pk=id), usuario=usuario, visivel=visivel, modalidade_do_curso=modalidade_do_curso, nome_do_curso=nome_do_curso, ano=ano, semestre=semestre, link_1=link_1)
                evento.save()
                print("Grade de horários Cadastrado com Sucesso")
                return render(request, 'usuarios/cadastrado_com_sucesso.html')
            except:
                print("Não foi possível incluir no banco de dados")
                return render(request, 'usuarios/nao_foi_cadastrado.html')
            
        # CALENDÁRIO ACADÊMICO - BANCO DE DADOS
        elif categoria == "Calendário acadêmico":
            usuario = request.POST['usuario']
            try:
                visivel = request.POST['visivel']
                visivel = True
            except:
                visivel = False
            nome_evento = request.POST['nome_evento']
            link_1 = request.POST['link_1']
            arquivo_1 = request.POST['arquivo_1']
            ano = request.POST['ano']
            
            if not nome_evento.strip():
                print('O campo nome evento não pode ficar em branco')
                return redirect('nao_foi_cadastrado')            
            if not link_1.strip():
                print('O campo link 1 não pode ficar em branco')
                return redirect('nao_foi_cadastrado')            
            if not arquivo_1.strip():
                print('O campo arquivo 1 não pode ficar em branco')
                return redirect('nao_foi_cadastrado')            
            if not ano.strip():
                print('O campo ano não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            try:
                evento = Evento.objects.create(categoria=Categorias.objects.get(pk=id), usuario=usuario, visivel=visivel, nome_evento=nome_evento, link_1=link_1, arquivo_1=arquivo_1, ano=ano)
                evento.save()
                print("Calendário acadêmico Cadastrado com Sucesso")
                return render(request, 'usuarios/cadastrado_com_sucesso.html')
            except:
                print("Não foi possível incluir no banco de dados")
                return render(request, 'usuarios/nao_foi_cadastrado.html')
        
        # INFORMAÇÕES RELEVANTES DOS CURSOS - BANCO DE DADOS
        elif categoria == "Informações relevantes dos cursos":
            usuario = request.POST['usuario']
            try:
                visivel = request.POST['visivel']
                visivel = True
            except:
                visivel = False                
            modalidade_do_curso = request.POST['modalidade_do_curso']
            nome_do_curso = request.POST['nome_do_curso']
            descricao = request.POST['descricao']
            forma_de_ingresso = request.POST['forma_de_ingresso']
            requisitos = request.POST['requisitos']
            turno = request.POST['turno']
            numero_de_vagas = request.POST['numero_de_vagas']
            coordenador_do_curso = request.POST['coordenador_do_curso']
            email_do_coordenador = request.POST['email_do_coordenador']
            email_do_curso = request.POST['email_do_curso']
            
            if not modalidade_do_curso.strip():
                print('O campo modalidade_do_curso não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not nome_do_curso.strip():
                print('O campo nome_do_curso não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not descricao.strip():
                print('O campo descricao não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not forma_de_ingresso.strip():
                print('O campo forma_de_ingresso não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not requisitos.strip():
                print('O campo requisitos não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not turno.strip():
                print('O campo turno não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not numero_de_vagas.strip():
                print('O campo numero_de_vagas não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not coordenador_do_curso.strip():
                print('O campo coordenador_do_curso não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not email_do_coordenador.strip():
                print('O campo email_do_coordenador não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not email_do_curso.strip():
                print('O campo email_do_curso não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            try:
                evento = Evento.objects.create(categoria=Categorias.objects.get(pk=id), usuario=usuario, visivel=visivel, modalidade_do_curso=modalidade_do_curso, nome_do_curso=nome_do_curso, descricao=descricao, forma_de_ingresso=forma_de_ingresso, requisitos=requisitos, turno=turno, numero_de_vagas=numero_de_vagas, coordenador_do_curso=coordenador_do_curso, email_do_coordenador=email_do_coordenador, email_do_curso=email_do_curso)
                evento.save()
                print("Informações relevantes dos cursos Cadastrado com Sucesso")
                return render(request, 'usuarios/cadastrado_com_sucesso.html')
            except:
                print("Não foi possível incluir no banco de dados")
                return render(request, 'usuarios/nao_foi_cadastrado.html')
            
        # INFORMAÇÕES SOBRE INSCRIÇÃO/MATRÍCULA - BANCO DE DADOS
        elif categoria == "Informações sobre inscrição/matrícula":
            usuario = request.POST['usuario']
            try:
                visivel = request.POST['visivel']
                visivel = True
            except:
                visivel = False
            nome_evento = request.POST['nome_evento']
            descricao = request.POST['descricao']
            link_1 = request.POST['link_1']
            try:
                link_2 = request.POST['link_2']            
            except:
                link_2 = ""
            try:
                link_3 = request.POST['link_3']            
            except:
                link_3 = ""
            try:
                arquivo_1 = request.POST['arquivo_1']            
            except:
                arquivo_1 = ""
            try:
                arquivo_2 = request.POST['arquivo_2']            
            except:
                arquivo_2 = ""
            try:
                arquivo_3 = request.POST['arquivo_3']            
            except:
                arquivo_3 = ""
            
            if not nome_evento.strip():
                print('O campo nome_evento não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not descricao.strip():
                print('O campo descricao não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not link_1.strip():
                print('O campo link_1 não pode ficar em branco')
                return redirect('nao_foi_cadastrado')            
            try:
                evento = Evento.objects.create(categoria=Categorias.objects.get(pk=id), usuario=usuario, visivel=visivel, nome_evento=nome_evento, descricao=descricao, link_1=link_1, link_2=link_2, link_3=link_3, arquivo_1=arquivo_1, arquivo_2=arquivo_2, arquivo_3=arquivo_3)
                evento.save()
                print("Informações sobre inscrição/matrícula Cadastrado com Sucesso")
                return render(request, 'usuarios/cadastrado_com_sucesso.html')
            except:
                print("Não foi possível incluir no banco de dados")
                return render(request, 'usuarios/nao_foi_cadastrado.html')
        
        # INFORMAÇÕES SOBRE REMATRÍCULA - BANCO DE DADOS
        elif categoria == "Informações sobre rematrícula":
            usuario = request.POST['usuario']
            try:
                visivel = request.POST['visivel']
                visivel = True
            except:
                visivel = False
            modalidade_do_curso = request.POST['modalidade_do_curso']
            nome_do_curso = request.POST['nome_do_curso']
            data_de_inicio = request.POST['data_de_inicio']
            data_de_fim = request.POST['data_de_fim']
            link_1 = request.POST['link_1']
            try:
                link_2 = request.POST['link_2']            
            except:
                link_2 = ""
            try:
                link_3 = request.POST['link_3']            
            except:
                link_3 = ""            
            if not modalidade_do_curso.strip():
                print('O campo modalidade_do_curso não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not nome_do_curso.strip():
                print('O campo nome_do_curso não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not data_de_inicio.strip():
                print('O campo data_de_inicio não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not data_de_fim.strip():
                print('O campo data_de_fim não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not link_1.strip():
                print('O campo link_1 não pode ficar em branco')
                return redirect('nao_foi_cadastrado')            
            try:
                evento = Evento.objects.create(categoria=Categorias.objects.get(pk=id), usuario=usuario, visivel=visivel, modalidade_do_curso=modalidade_do_curso, nome_do_curso=nome_do_curso, data_de_inicio=data_de_inicio, data_de_fim=data_de_fim, link_1=link_1, link_2=link_2, link_3=link_3)
                evento.save()
                print("Informações sobre rematrícula Cadastrado com Sucesso")
                return render(request, 'usuarios/cadastrado_com_sucesso.html')
            except:
                print("Não foi possível incluir no banco de dados")
                return render(request, 'usuarios/nao_foi_cadastrado.html')
        
        # REQUERIMENTOS/FORMULÁRIOS - BANCO DE DADOS
        elif categoria == "Requerimentos/formulários":
            usuario = request.POST['usuario']
            try:
                visivel = request.POST['visivel']
                visivel = True
            except:
                visivel = False
            nome_do_requerimento = request.POST['nome_do_requerimento']
            descricao = request.POST['descricao']
            data_de_inicio = request.POST['data_de_inicio']
            data_de_fim = request.POST['data_de_fim']
            link_1 = request.POST['link_1']
            try:
                link_2 = request.POST['link_2']            
            except:
                link_2 = ""
            try:
                arquivo_1 = request.POST['arquivo_1']            
            except:
                arquivo_1 = ""
            try:
                arquivo_2 = request.POST['arquivo_2']            
            except:
                arquivo_2 = ""
            try:
                foto_1 = request.POST['foto_1']            
            except:
                foto_1 = ""
            try:
                foto_2 = request.POST['foto_2']            
            except:
                foto_2 = ""
            if not nome_do_requerimento.strip():
                print('O campo nome_do_requerimento não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not descricao.strip():
                print('O campo descricao não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not data_de_inicio.strip():
                print('O campo data_de_inicio não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not data_de_fim.strip():
                print('O campo data_de_fim não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not link_1.strip():
                print('O campo link_1 não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            try:
                evento = Evento.objects.create(categoria=Categorias.objects.get(pk=id), usuario=usuario, visivel=visivel, nome_do_requerimento=nome_do_requerimento, descricao=descricao, data_de_inicio=data_de_inicio, data_de_fim=data_de_fim, link_1=link_1, link_2=link_2, arquivo_1=arquivo_1, arquivo_2=arquivo_2, foto_1=foto_1, foto_2=foto_2)
                evento.save()
                print("Requerimentos/formulários Cadastrado com Sucesso")
                return render(request, 'usuarios/cadastrado_com_sucesso.html')
            except:
                print("Não foi possível incluir no banco de dados")
                return render(request, 'usuarios/nao_foi_cadastrado.html')
        
        # TUTORIAIS DE ACESSOS A SISTEMAS ACADÊMICOS - BANCO DE DADOS
        elif categoria == "Tutoriais de acessos a sistemas acadêmicos":
            usuario = request.POST['usuario']
            try:
                visivel = request.POST['visivel']
                visivel = True
            except:
                visivel = False
            nome_do_sistema = request.POST['nome_do_sistema']
            descricao = request.POST['descricao']
            link_1 = request.POST['link_1']
            try:
                link_2 = request.POST['link_2']            
            except:
                link_2 = ""
            try:
                arquivo_1 = request.POST['arquivo_1']            
            except:
                arquivo_1 = ""
            try:
                arquivo_2 = request.POST['arquivo_2']            
            except:
                arquivo_2 = ""            
            if not nome_do_sistema.strip():
                print('O campo nome_do_sistema não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not descricao.strip():
                print('O campo descricao não pode ficar em branco')
                return redirect('nao_foi_cadastrado')
            if not link_1.strip():
                print('O campo link_1 não pode ficar em branco')
                return redirect('nao_foi_cadastrado')            
            try:
                evento = Evento.objects.create(categoria=Categorias.objects.get(pk=id), usuario=usuario, visivel=visivel, nome_do_sistema=nome_do_sistema, descricao=descricao, link_1=link_1, link_2=link_2, arquivo_1=arquivo_1, arquivo_2=arquivo_2)
                evento.save()
                print("Tutoriais de acessos a sistemas acadêmicos Cadastrado com Sucesso")
                return render(request, 'usuarios/cadastrado_com_sucesso.html')
            except:
                print("Não foi possível incluir no banco de dados")
                return render(request, 'usuarios/nao_foi_cadastrado.html')
            
        else:
            return render(request, 'usuarios/nao_foi_cadastrado.html')
                
def cadastrado_com_sucesso(request):
    categorias = Categorias.objects.all()
    dados = {
        'categorias': categorias
    }
    if request.user.is_authenticated:
        return render(request, 'usuarios/cadastrado_com_sucesso.html', dados)
    else:
        return redirect('index')

def nao_foi_cadastrado(request):
    categorias = Categorias.objects.all()
    dados = {
        'categorias': categorias
    }
    if request.user.is_authenticated:
        return render(request, 'usuarios/nao_foi_cadastrado.html', dados)
    else:
        return redirect('index')