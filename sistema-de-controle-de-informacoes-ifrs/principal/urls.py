from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from api.views import EventosViewSet, comprovante_de_matriculaViewSet, contato_dos_professoresViewSet, grade_de_horariosViewSet, calendario_academicoViewSet, informacoes_relevantes_dos_cursosViewSet, informacoes_sobre_inscricao_ou_matriculaViewSet, informacoes_sobre_rematriculaViewSet, requerimentos_ou_formulariosViewSet, tutoriais_de_acessos_a_sistemas_academicosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('eventos',EventosViewSet, basename='Eventos')
router.register('comprovante_de_matricula',comprovante_de_matriculaViewSet, basename='comprovante_de_matricula')
router.register('contato_dos_professores',contato_dos_professoresViewSet, basename='contato_dos_professores')
router.register('grade_de_horarios',grade_de_horariosViewSet, basename='grade_de_horarios')
router.register('calendario_academico',calendario_academicoViewSet, basename='calendario_academico')
router.register('informacoes_relevantes_dos_cursos',informacoes_relevantes_dos_cursosViewSet, basename='informacoes_relevantes_dos_cursos')
router.register('informacoes_sobre_inscricao_ou_matricula',informacoes_sobre_inscricao_ou_matriculaViewSet, basename='informacoes_sobre_inscricao_ou_matricula')
router.register('informacoes_sobre_rematricula',informacoes_sobre_rematriculaViewSet, basename='informacoes_sobre_rematricula')
router.register('requerimentos_ou_formularios',requerimentos_ou_formulariosViewSet, basename='requerimentos_ou_formularios')
router.register('tutoriais_de_acessos_a_sistemas_academicos',tutoriais_de_acessos_a_sistemas_academicosViewSet, basename='tutoriais_de_acessos_a_sistemas_academicos')



urlpatterns = [
    path('', include('app.urls')),
    path('api/', include(router.urls)),
    path('usuarios/', include('usuarios.urls')),
    path('categorias/', include('categorias.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )