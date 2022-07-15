from django.contrib import admin
from .models import Calendario
from .models import Categoria

class ListandoEventos(admin.ModelAdmin):
    list_display = ('id', 'nome_evento', 'categoria_evento', 'data_atualizacao', 'data_evento', 'visivel')
    list_display_links = ('id', 'nome_evento')
    search_fields = ('nome_evento',)
    list_filter = ('categoria_evento',)
    list_editable = ('visivel',)
    list_per_page = 30


admin.site.register(Calendario, ListandoEventos)
admin.site.register(Categoria)