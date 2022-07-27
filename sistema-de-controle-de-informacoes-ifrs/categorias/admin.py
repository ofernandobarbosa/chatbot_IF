from django.contrib import admin
from .models import Categorias


class ListandoCategorias(admin.ModelAdmin):
    list_display = ('id', 'nome_categoria', 'visivel')
    list_display_links = ('id', 'nome_categoria')
    search_fields = ('nome_categoria',)
    list_editable = ('visivel',)

admin.site.register(Categorias, ListandoCategorias)
