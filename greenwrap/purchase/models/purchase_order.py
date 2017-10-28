from django.conf import settings
from django.db import models

from product.models import Product, ProductOption
from utils.models import Model
from .purchase import Purchase

__all__ = (
    'PurchaseOrder',
)


class PurchaseOrder(Model):
    """
    주문정보
    """
    purchase = models.ForeignKey(Purchase)
    product = models.ForeignKey(Product)
    option = models.ForeignKey(ProductOption)
    quantity = models.PositiveSmallIntegerField(default=1)

    class Meta:
        verbose_name = '주문항목'
        verbose_name_plural = '%s 목록' % verbose_name

    def __str__(self):
        return '주문항목 (주문정보pk: {}, 주문자: {}, 상품: {}, 옵션: {}, 수량: {}'.format(
            self.purchase.pk,
            self.purchase.owner,
            self.product.title,
            self.option.title,
            self.quantity,d
        )
