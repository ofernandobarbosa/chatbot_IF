from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
 	path('calendario/<int:calendario_id>' , views.calendario, name='calendario'),
  	path('categoria/<int:categoria_id>', views.categoria, name='categoria'),
   	path('buscar', views.buscar, name = 'buscar'),
]