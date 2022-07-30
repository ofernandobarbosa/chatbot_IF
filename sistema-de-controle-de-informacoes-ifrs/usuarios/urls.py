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