from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
 	path('evento/<int:evento_id>' , views.evento, name='evento'),
  	path('categoria/<int:categoria_id>', views.categoria, name='categoria'),
   	path('buscar', views.buscar, name = 'buscar'),
]