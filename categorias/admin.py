from django.contrib import admin
from . import models


# @register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cat',)
    list_display_links = ('nome_cat',)


admin.site.register(models.Categoria, CategoriaAdmin)