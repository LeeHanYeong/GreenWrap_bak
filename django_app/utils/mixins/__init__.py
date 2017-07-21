from django.db import models

from ..models import Model


class SortableMixin(Model):
    _order = models.PositiveIntegerField('순서', default=0, blank=False, null=False)

    class Meta:
        abstract = True
        ordering = ['_order',]
