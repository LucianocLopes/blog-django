from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils import timezone

from posts.models import Post


class Comentario(models.Model):
    nome_comentario = models.CharField(
        verbose_name=_('nome'),
        max_length=255,
    )
    email_comentario = models.EmailField(
        verbose_name=_('email'),
    )
    comentario = models.TextField(
        verbose_name=_('comentario'),
    )
    post_comentario = models.ForeignKey(
        Post,
        verbose_name=_('post'),
        related_name='comentario_post',
        on_delete=models.CASCADE,
    )
    usuario_comentario = models.ForeignKey(
        get_user_model(),
        verbose_name=_('usuario'),
        related_name='comentario_user',
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    data_comentario = models.DateTimeField(
        verbose_name=_('data'),
        default=timezone.now,
    )
    publicado_comentario = models.BooleanField(
        verbose_name=_('publicado'),
        default=False
    )

    def __str__(self) -> str:
        return f'Comentário de {self.nome_comentario.strip().title()} do \
            post {self.post_comentario} feito em {self.data_comentario}'
