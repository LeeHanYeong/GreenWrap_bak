from django.db import models
from django.utils import timezone

from utils.exceptions import PriceDoesNotExist, PriceError
from utils.mixins import SortableMixin
from .product import Product
from utils.models import Model, BasePrice

__all__ = (
    'ProductOption',
    'ProductOptionPrice',
)


class ProductOption(SortableMixin, Model):
    """
    상품 특징
        하나의 상품이 특징에 따라 여러 상품으로 나누어지는 단위
        Product와 MTO으로 매칭
            ex) 6mm, 8mm...등
    """
    product = models.ForeignKey(
        Product,
        verbose_name='상품',
        related_name='option_set',
    )
    title = models.CharField('옵션명', max_length=100)
    quantity = models.PositiveSmallIntegerField('단위수량', default=1)

    class Meta(SortableMixin.Meta):
        verbose_name = '상품 옵션'
        verbose_name_plural = '%s 목록' % verbose_name

    def __str__(self):
        return '{product} 옵션 (옵션명: {title}, 가격: {price:,d}원)'.format(
            product=self.product.title,
            title=self.title,
            price=self.price
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.price_set.exists():
            self.price_set.create()

    @property
    def price(self):
        return self.get_price_instance().price

    def get_price_instance(self):
        if not self.price_set.exists():
            try:
                self.save()
            except:
                raise PriceDoesNotExist(self)
        try:
            return self.price_set.first()
        except Exception as e:
            raise PriceError(self, e)


class ProductOptionPrice(BasePrice):
    product_option = models.ForeignKey(
        ProductOption,
        verbose_name='상품 옵션',
        related_name='price_set'
    )

    class Meta(BasePrice.Meta):
        verbose_name = '상품 옵션 가격'
        verbose_name_plural = '%s 목록' % verbose_name

    def __str__(self):
        return '{product} 옵션 ({option_title}) 가격 ({price:,d}원) [{start_date}~]'.format(
            product=self.product_option.product.title,
            option_title=self.product_option.title,
            price=self.price,
            start_date=self.start_date
        )
