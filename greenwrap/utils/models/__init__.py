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
    start_date = models.DateField('시작일자', default=timezone.now)
    price = models.IntegerField('단위가격', default=0)

    class Meta:
        abstract = True
        ordering = ['-start_date']

    def __str__(self):
        return '{price:,d} [{start_date}~]'.format(
            price=self.price,
            start_date=self.start_date
        )
