from django.db import models
from django.db.models import Model as DjangoModel
from django.utils import timezone

__all__ = (
    'Model',
    'BasePrice',
)


class Model(DjangoModel):
    class Meta:
        abstract = True


class BasePrice(Model):
    start_date = models.DateField(default=timezone.now)
    price = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return '{price:,d} [{start_date}~]'.format(
            price=self.price,
            start_date=self.start_date
        )
