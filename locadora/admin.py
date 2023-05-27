from django.contrib import admin
from .models import Categoria, Filme, Locacao

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'valor', 'categoria')

class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'cliente')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Filme, FilmeAdmin)
admin.site.register(Locacao, LocacaoAdmin)
