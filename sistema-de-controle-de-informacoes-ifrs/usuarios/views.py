from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from categorias.models import Categorias
from app.models import Evento
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.http import HttpResponseRedirect

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
            messages.error(request, 'O campo nome não pode ficar em branco')
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            messages.error(request, 'O campo e-mail não pode ficar em branco')
            print('O campo e-mail não pode ficar em branco')
            return redirect('cadastro')
        if not password.strip():
            messages.error(request, 'O campo senha não pode ficar em branco')
            print('O campo senha não pode ficar em branco')
            return redirect('cadastro')
        if not password2.strip():
            messages.error(request, 'O campo confirmação da senha não pode ficar em branco')
            print('O campo confirmação da senha não pode ficar em branco')
            return redirect('cadastro')
        if password != password2:
            messages.error(request, 'As senhas digitadas não conferem')
            print('As senhas digitadas não conferem')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            print('Usuário já cadastrado')
            return redirect('cadastro')
        nome = nome.title()
        user = User.objects.create_user(
            username=nome, email=email, password=password)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso')
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
            messages.error(request, 'os campos email e senha não podem ficar em branco')
            print('os campos email e senha não podem ficar em branco')
            return redirect('login')
        elif User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list(
                'username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'login realizado com sucesso')
                print('login realizado com sucesso')
                return redirect('dashboard')
            else:
                messages.error(request, 'Não foi possível realizar este login')
                print('Não foi possível realizar este login')
                return redirect('login')
        else:
            messages.error(request, 'Email não localizado')
            print('Email não localizado')
            return redirect('login')
    else:
        return render(request, 'usuarios/login.html', dados)

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    categorias = Categorias.objects.all()
    eventos = Evento.objects.order_by('-data_atualizacao')
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
    eventos = Evento.objects.all()
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
                messages.error(request, 'O campo nome do professor não pode ficar em branco')
                print('O campo nome do professor não pode ficar em branco')
                return redirect('dashboard')
            if not email.strip():
                messages.error(request, 'O campo email não pode ficar em branco')
                print('O campo email não pode ficar em branco')
                return redirect('dashboard')
            if not nome_da_disciplina.strip():
                messages.error(request, 'O campo nome da disciplina não pode ficar em branco')
                print('O campo nome da disciplina não pode ficar em branco')
                return redirect('dashboard')
            nome_do_professor = nome_do_professor.title()
            nome_completo = nome_do_professor.split()
            nome_do_professor = nome_completo[0]
            nome_completo.pop(0)
            sobrenome_do_professor = " ".join(nome_completo)
            nome_da_disciplina = nome_da_disciplina.title()
            try:
                evento = Evento.objects.create(categoria=Categorias.objects.get(pk=id), usuario=usuario, nome_do_professor=nome_do_professor, sobrenome_do_professor=sobrenome_do_professor, email=email, nome_da_disciplina=nome_da_disciplina, visivel=visivel)
                evento.save()
                messages.success(request, 'Contato do Professor Cadastrado com Sucesso')
                print("Contato do Professor Cadastrado com Sucesso")
                return render(request, 'usuarios/dashboard.html')
            except:
                messages.error(request, 'Não foi possível incluir no banco de dados')
                print("Não foi possível incluir no banco de dados")
                return render(request, 'usuarios/dashboard.html')
        
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
                messages.error(request, 'O campo nome evento não pode ficar em branco')
                print('O campo nome evento não pode ficar em branco')
                return redirect('dashboard')
            if not link_1.strip():
                messages.error(request, 'O campo link 1 não pode ficar em branco')
                print('O campo link 1 não pode ficar em branco')
                return redirect('dashboard')
            try:
                nome_evento = nome_evento.title()
                evento = Evento.objects.create(categoria=Categorias.objects.get(pk=id), usuario=usuario, nome_evento=nome_evento, link_1=link_1, link_2=link_2, link_3=link_3, visivel=visivel)
                evento.save()
                messages.success(request, 'Comprovante de Matrícula Cadastrado com Sucesso')
                print("Comprovante de Matrícula Cadastrado com Sucesso")
                return render(request, 'usuarios/dashboard.html')
            except:
                messages.error(request, 'Não foi possível incluir no banco de dados')
                print("Não foi possível incluir no banco de dados")
                return render(request, 'usuarios/dashboard.html')
            
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
                messages.error(request, 'O campo modalidade do curso não pode ficar em branco')
                print('O campo modalidade do curso não pode ficar em branco')
                return redirect('dashboard')
            if not nome_do_curso.strip():
                messages.error(request, 'O campo nome do curso não pode ficar em branco')
                print('O campo nome do curso não pode ficar em branco')
                return redirect('dashboard')
            if not ano.strip():
                messages.error(request, 'O campo ano não pode ficar em branco')
                print('O campo ano não pode ficar em branco')
                return redirect('dashboard')
            if not semestre.strip():
                messages.error(request, 'O campo semestre não pode ficar em branco')
                print('O campo semestre não pode ficar em branco')
                return redirect('dashboard')
            if not link_1.strip():
                messages.error(request, 'O campo link 1 não pode ficar em branco')
                print('O campo link 1 não pode ficar em branco')
                return redirect('dashboard')            
            try:
                nome_do_curso = nome_do_curso.title()
                modalidade_do_curso = modalidade_do_curso.title()
                evento = Evento.objects.create(categoria=Categorias.objects.get(pk=id), usuario=usuario, visivel=visivel, modalidade_do_curso=modalidade_do_curso, nome_do_curso=nome_do_curso, ano=ano, semestre=semestre, link_1=link_1)
                evento.save()
                messages.success(request, 'Grade de horários Cadastrado com Sucesso')
                print("Grade de horários Cadastrado com Sucesso")
                return render(request, 'usuarios/dashboard.html')
            except:
                messages.error(request, 'Não foi possível incluir no banco de dados')
                print("Não foi possível incluir no banco de dados")
                return render(request, 'usuarios/dashboard.html')
            
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
            arquivo_1 = request.FILES['arquivo_1']
            ano = request.POST['ano']
            
            if not nome_evento.strip():
                messages.error(request, 'O campo nome evento não pode ficar em branco')
                print('O campo nome evento não pode ficar em branco')
                return redirect('dashboard')            
            if not link_1.strip():
                messages.error(request, 'O campo link 1 não pode ficar em branco')
                print('O campo link 1 não pode ficar em branco')
                return redirect('dashboard')           
            if not ano.strip():
                messages.error(request, 'O campo ano não pode ficar em branco')
                print('O campo ano não pode ficar em branco')
                return redirect('dashboard')
            try:
                nome_evento = nome_evento.title()
                evento = Evento.objects.create(categoria=Categorias.objects.get(pk=id), usuario=usuario, visivel=visivel, nome_evento=nome_evento, link_1=link_1, arquivo_1=arquivo_1, ano=ano)
                evento.save()
                messages.success(request, 'Calendário acadêmico Cadastrado com Sucesso')
                print("Calendário acadêmico Cadastrado com Sucesso")
                return render(request, 'usuarios/dashboard.html')
            except:
                messages.error(request, 'Não foi possível incluir no banco de dados')
                print("Não foi possível incluir no banco de dados")
                return render(request, 'usuarios/dashboard.html')
        
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
                messages.error(request, 'O campo modalidade_do_curso não pode ficar em branco')
                print('O campo modalidade_do_curso não pode ficar em branco')
                return redirect('dashboard')
            if not nome_do_curso.strip():
                messages.error(request, 'O campo nome_do_curso não pode ficar em branco')
                print('O campo nome_do_curso não pode ficar em branco')
                return redirect('dashboard')
            if not descricao.strip():
                messages.error(request, 'O campo descricao não pode ficar em branco')
                print('O campo descricao não pode ficar em branco')
                return redirect('dashboard')
            if not forma_de_ingresso.strip():
                messages.error(request, 'O campo forma_de_ingresso não pode ficar em branco')
                print('O campo forma_de_ingresso não pode ficar em branco')
                return redirect('dashboard')
            if not requisitos.strip():
                messages.error(request, 'O campo requisitos não pode ficar em branco')
                print('O campo requisitos não pode ficar em branco')
                return redirect('dashboard')
            if not turno.strip():
                messages.error(request, 'O campo turno não pode ficar em branco')
                print('O campo turno não pode ficar em branco')
                return redirect('dashboard')
            if not numero_de_vagas.strip():
                messages.error(request, 'O campo numero_de_vagas não pode ficar em branco')
                print('O campo numero_de_vagas não pode ficar em branco')
                return redirect('dashboard')
            if not coordenador_do_curso.strip():
                messages.error(request, 'O campo coordenador_do_curso não pode ficar em branco')
                print('O campo coordenador_do_curso não pode ficar em branco')
                return redirect('dashboard')
            if not email_do_coordenador.strip():
                messages.error(request, 'O campo email_do_coordenador não pode ficar em branco')
                print('O campo email_do_coordenador não pode ficar em branco')
                return redirect('dashboard')
            if not email_do_curso.strip():
                messages.error(request, 'O campo email_do_curso não pode ficar em branco')
                print('O campo email_do_curso não pode ficar em branco')
                return redirect('dashboard')
            try:
                nome_do_curso = nome_do_curso.title()
                modalidade_do_curso = modalidade_do_curso.title()
                coordenador_do_curso = coordenador_do_curso.title()
                evento = Evento.objects.create(categoria=Categorias.objects.get(pk=id), usuario=usuario, visivel=visivel, modalidade_do_curso=modalidade_do_curso, nome_do_curso=nome_do_curso, descricao=descricao, forma_de_ingresso=forma_de_ingresso, requisitos=requisitos, turno=turno, numero_de_vagas=numero_de_vagas, coordenador_do_curso=coordenador_do_curso, email_do_coordenador=email_do_coordenador, email_do_curso=email_do_curso)
                evento.save()
                messages.success(request, 'Informações relevantes dos cursos Cadastrado com Sucesso')
                print("Informações relevantes dos cursos Cadastrado com Sucesso")
                return render(request, 'usuarios/dashboard.html')
            except:
                messages.error(request, 'Não foi possível incluir no banco de dados')
                print("Não foi possível incluir no banco de dados")
                return render(request, 'usuarios/dashboard.html')
            
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
            modalidade_de_ingresso = request.POST['modalidade_de_ingresso']
            try:
                link_2 = request.POST['link_2']            
            except:
                link_2 = ""
            try:
                link_3 = request.POST['link_3']            
            except:
                link_3 = ""
            try:
                arquivo_1 = request.FILES['arquivo_1']            
            except:
                arquivo_1 = ""
            try:
                arquivo_2 = request.FILES['arquivo_2']            
            except:
                arquivo_2 = ""
            try:
                arquivo_3 = request.FILES['arquivo_3']            
            except:
                arquivo_3 = ""
            
            if not nome_evento.strip():
                messages.error(request, 'O campo nome_evento não pode ficar em branco')
                print('O campo nome_evento não pode ficar em branco')
                return redirect('dashboard')
            if not descricao.strip():
                messages.error(request, 'O campo descricao não pode ficar em branco')
                print('O campo descricao não pode ficar em branco')
                return redirect('dashboard')
            if not link_1.strip():
                messages.error(request, 'O campo link_1 não pode ficar em branco')
                print('O campo link_1 não pode ficar em branco')
                return redirect('dashboard')            
            try:
                nome_evento = nome_evento.title()
                evento = Evento.objects.create(categoria=Categorias.objects.get(pk=id), usuario=usuario, visivel=visivel, modalidade_de_ingresso=modalidade_de_ingresso, nome_evento=nome_evento, descricao=descricao, link_1=link_1, link_2=link_2, link_3=link_3, arquivo_1=arquivo_1, arquivo_2=arquivo_2, arquivo_3=arquivo_3)
                evento.save()
                messages.success(request, 'Informações sobre inscrição/matrícula Cadastrado com Sucesso')
                print("Informações sobre inscrição/matrícula Cadastrado com Sucesso")
                return render(request, 'usuarios/dashboard.html')
            except:
                messages.error(request, 'Não foi possível incluir no banco de dados')
                print("Não foi possível incluir no banco de dados")
                return render(request, 'usuarios/dashboard.html')
        
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
                messages.error(request, 'O campo modalidade_do_curso não pode ficar em branco')
                print('O campo modalidade_do_curso não pode ficar em branco')
                return redirect('dashboard')
            if not nome_do_curso.strip():
                messages.error(request, 'O campo nome_do_curso não pode ficar em branco')
                print('O campo nome_do_curso não pode ficar em branco')
                return redirect('dashboard')
            if not data_de_inicio.strip():
                messages.error(request, 'O campo data_de_inicio não pode ficar em branco')
                print('O campo data_de_inicio não pode ficar em branco')
                return redirect('dashboard')
            if not data_de_fim.strip():
                messages.error(request, 'OO campo data_de_fim não pode ficar em branco')
                print('O campo data_de_fim não pode ficar em branco')
                return redirect('dashboard')
            if not link_1.strip():
                messages.error(request, 'O campo link_1 não pode ficar em branco')
                print('O campo link_1 não pode ficar em branco')
                return redirect('dashboard')            
            try:
                ano = data_de_inicio[0]+data_de_inicio[1]+data_de_inicio[2]+data_de_inicio[3]
                mes = data_de_inicio[5]+data_de_inicio[6]
                dia = data_de_inicio[8]+data_de_inicio[9]
                data_de_inicio = f'{dia}/{mes}/{ano}'
                ano = data_de_fim[0]+data_de_fim[1]+data_de_fim[2]+data_de_fim[3]
                mes = data_de_fim[5]+data_de_fim[6]
                dia = data_de_fim[8]+data_de_fim[9]
                data_de_fim = f'{dia}/{mes}/{ano}'
                nome_do_curso = nome_do_curso.title()
                modalidade_do_curso = modalidade_do_curso.title()
                evento = Evento.objects.create(categoria=Categorias.objects.get(pk=id), usuario=usuario, visivel=visivel, modalidade_do_curso=modalidade_do_curso, nome_do_curso=nome_do_curso, data_de_inicio=data_de_inicio, data_de_fim=data_de_fim, link_1=link_1, link_2=link_2, link_3=link_3)
                evento.save()
                messages.success(request, 'Informações sobre rematrícula Cadastrado com Sucesso')
                print("Informações sobre rematrícula Cadastrado com Sucesso")
                return render(request, 'usuarios/dashboard.html')
            except:
                messages.error(request, 'Não foi possível incluir no banco de dados')
                print("Não foi possível incluir no banco de dados")
                return render(request, 'usuarios/dashboard.html')
        
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
            print (data_de_inicio)
            try:
                link_2 = request.POST['link_2']            
            except:
                link_2 = ""
            try:
                arquivo_1 = request.FILES['arquivo_1']            
            except:
                arquivo_1 = ""
            try:
                arquivo_2 = request.FILES['arquivo_2']            
            except:
                arquivo_2 = ""
            try:
                foto_1 = request.FILES['foto_1']            
            except:
                foto_1 = ""
            try:
                foto_2 = request.FILES['foto_2']            
            except:
                foto_2 = ""
            if not nome_do_requerimento.strip():
                messages.error(request, 'O campo nome do requerimento não pode ficar em branco')
                print('O campo nome do requerimento não pode ficar em branco')
                return redirect('dashboard')
            if not descricao.strip():
                messages.error(request, 'O campo descrição não pode ficar em branco')
                print('O campo descricao não pode ficar em branco')
                return redirect('dashboard')
            if not data_de_inicio.strip():
                messages.error(request, 'O campo data de início não pode ficar em branco')
                print('O campo data_de_inicio não pode ficar em branco')
                return redirect('dashboard')
            if not data_de_fim.strip():
                messages.error(request, 'O campo data de fim não pode ficar em branco')
                print('O campo data_de_fim não pode ficar em branco')
                return redirect('dashboard')
            if not link_1.strip():
                messages.error(request, 'O campo link 1 não pode ficar em branco')
                print('O campo link_1 não pode ficar em branco')
                return redirect('dashboard')
            try:
                ano = data_de_inicio[0]+data_de_inicio[1]+data_de_inicio[2]+data_de_inicio[3]
                mes = data_de_inicio[5]+data_de_inicio[6]
                dia = data_de_inicio[8]+data_de_inicio[9]
                data_de_inicio = f'{dia}/{mes}/{ano}'
                ano = data_de_fim[0]+data_de_fim[1]+data_de_fim[2]+data_de_fim[3]
                mes = data_de_fim[5]+data_de_fim[6]
                dia = data_de_fim[8]+data_de_fim[9]
                data_de_fim = f'{dia}/{mes}/{ano}'
                nome_do_requerimento = nome_do_requerimento.title()
                evento = Evento.objects.create(categoria=Categorias.objects.get(pk=id), usuario=usuario, visivel=visivel, nome_do_requerimento=nome_do_requerimento, descricao=descricao, data_de_inicio=data_de_inicio, data_de_fim=data_de_fim, link_1=link_1, link_2=link_2, arquivo_1=arquivo_1, arquivo_2=arquivo_2, foto_1=foto_1, foto_2=foto_2)
                evento.save()
                messages.success(request, 'Requerimentos/formulários Cadastrado com Sucesso')
                print("Requerimentos/formulários Cadastrado com Sucesso")
                return render(request, 'usuarios/dashboard.html')
            except:
                messages.error(request, 'Não foi possível incluir no banco de dados')
                print("Não foi possível incluir no banco de dados")
                return render(request, 'usuarios/dashboard.html')
        
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
            if not nome_do_sistema.strip():
                messages.error(request, 'O campo nome_do_sistema não pode ficar em branco')
                print('O campo nome do sistema não pode ficar em branco')
                return redirect('dashboard')
            if not descricao.strip():
                messages.error(request, 'O campo descricao não pode ficar em branco')
                print('O campo descrição não pode ficar em branco')
                return redirect('dashboard')
            if not link_1.strip():
                messages.error(request, 'O campo link_1 não pode ficar em branco')
                print('O campo link 1 não pode ficar em branco')
                return redirect('dashboard')            
            try:
                nome_do_sistema = nome_do_sistema.title()
                evento = Evento.objects.create(categoria=Categorias.objects.get(pk=id), usuario=usuario, visivel=visivel, nome_do_sistema=nome_do_sistema, descricao=descricao, link_1=link_1, link_2=link_2)
                evento.save()
                messages.success(request, 'Tutoriais de acessos a sistemas acadêmicos Cadastrado com Sucesso')
                print("Tutoriais de acessos a sistemas acadêmicos Cadastrado com Sucesso")
                return render(request, 'usuarios/dashboard.html')
            except:
                messages.error(request, 'Não foi possível incluir no banco de dados')
                print("Não foi possível incluir no banco de dados")
                return render(request, 'usuarios/dashboard.html')
            
        else:
            messages.error(request, 'Não foi possível incluir no banco de dados')
            return render(request, 'usuarios/dashboard.html')