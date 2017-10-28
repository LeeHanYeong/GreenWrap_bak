from django.conf import settings
from django.db import models

from utils.models import Model

__all__ = (
    'Purchase',
)


class Purchase(Model):
    """
    주문정보
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='주문자')
    created_date = models.DateTimeField('생성시간', auto_now_add=True)

    class Meta:
        verbose_name = '주문정보'
        verbose_name_plural = '%s 목록' % verbose_name

    def __str__(self):
        return '주문정보 (주문자: {}, 생성시간: {}'.format(
            self.owner,
            self.created_date
        )
