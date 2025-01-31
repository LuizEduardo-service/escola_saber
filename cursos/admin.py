from django.contrib import admin
from .models import Cursos, Avaliacao

# Register your models here.
@admin.register(Cursos)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'url', 'criacao', 'atualizacao', 'ativo']

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['curso', 'nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo']
