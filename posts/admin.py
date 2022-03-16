from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from . import models


class PostAdmin(SummernoteModelAdmin):
    list_display = (
        'id',
        'titulo_post',
        'autor_post',
        'data_post',
        'categoria_post',
        'publicado_post',
    )
    list_editable = ('publicado_post', )
    list_display_links = ('titulo_post',)
    summernote_fields = ('conteudo_post', )


admin.site.register(models.Post, PostAdmin)
# Register your models here.
