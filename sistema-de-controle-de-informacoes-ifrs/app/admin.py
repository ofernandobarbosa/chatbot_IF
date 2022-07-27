from django.contrib import admin
from .models import Evento
    
class ListandoEventosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_evento', 'categoria', 'data_atualizacao', 'usuario', 'visivel')
    list_display_links = ('id', 'nome_evento', 'categoria')
    search_fields = ('nome_evento','categoria','usuario')
    list_editable = ('visivel',)
    list_per_page = 30

admin.site.register(Evento, ListandoEventosAdmin)