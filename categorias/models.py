from django.db import models
from django.utils.translation import gettext_lazy as _

class Categoria(models.Model):
    nome_cat = models.CharField(
        verbose_name=_('categoria'),
        max_length=50,
    )

    def __str__(self) -> str:
        return self.nome_cat.strip().title()

