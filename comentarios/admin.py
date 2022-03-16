from django.contrib import admin
from . import models


class ComentarioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome_comentario',
        'email_comentario',
        'post_comentario',
        'data_comentario',
        'publicado_comentario',
    )
    list_editable = ('publicado_comentario', )
    list_display_links = ('nome_comentario',)


admin.site.register(models.Comentario, ComentarioAdmin)
