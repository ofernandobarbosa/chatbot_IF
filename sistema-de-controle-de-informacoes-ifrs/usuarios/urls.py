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
    path('cadastrado_com_sucesso', views.cadastrado_com_sucesso, name='cadastrado_com_sucesso'), 
    path('nao_foi_cadastrado', views.nao_foi_cadastrado, name='nao_foi_cadastrado'),       
]