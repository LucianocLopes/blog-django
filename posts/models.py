from email.mime import image
from hashlib import blake2b
from re import T
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils import timezone

from categorias.models import Categoria


class Post(models.Model):
    titulo_post = models.CharField(
        verbose_name=_('título'),
        max_length=255,
    )
    autor_post = models.ForeignKey(
        get_user_model(),
        verbose_name=_('autor'),
        related_name='post_user',
        on_delete=models.DO_NOTHING,
    )
    data_post = models.DateTimeField(
        verbose_name=_('data'),
        default=timezone.now,
    )
    conteudo_post = models.TextField(
        verbose_name=_('conteúdo'),
    )
    excerto_post = models.TextField(
        verbose_name=_('excerto'),
    )
    categoria_post = models.ForeignKey(
        Categoria,
        verbose_name=_('categoria'),
        related_name='post_categoria',
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    imagem_post = models.ImageField(
        verbose_name=_('imagem'),
        upload_to='post_img/%Y/%m/%d',
        blank=True,
        null=True,
    )
    publicado_post = models.BooleanField(
        verbose_name=_('publicado'),
        default=False,
    )


    def __str__(self) -> str:
        return self.titulo_post.strip().title()