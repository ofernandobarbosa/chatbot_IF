from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from api.views import Eventos_todos, comprovante_de_matricula, contato_dos_professores, grade_de_horarios, calendario_academico, informacoes_relevantes_dos_cursos, informacoes_sobre_inscricao_ou_matricula, informacoes_sobre_rematricula, requerimentos_ou_formularios, tutoriais_de_acessos_a_sistemas_academicos

urlpatterns = [
    path('', include('app.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('categorias/', include('categorias.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
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