from django.db import models

from utils.exceptions import PriceDoesNotExist, PriceError
from utils.mixins import SortableMixin
from utils.models import Model, BasePrice
from .product import Product

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
        return '{product} 옵션 (옵션명: {title}{quantity}, 가격: {price:,d}원{quantity_price})'.format(
            product=self.product.__str__(),
            title=self.title,
            quantity=f', 단위수량: {self.quantity:,d}' if not self.is_single_item() else '',
            price=self.price,
            quantity_price=f', 단위가격: {self.quantity_price:,d}원' if not self.is_single_item() else '',
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.price_set.exists():
            self.price_set.create()

    @property
    def quantity_price(self):
        """
        자신의 ProductOptionPrice의 가장 최신 항목의 가격
        옵션의 수량이 1일 경우, price와 같은 값을 가짐
        :return:
        """
        return self.get_price_instance().price

    @property
    def price(self):
        """
        자신의 ProductOptionPrice의 가장 최신 항목의 가격 * 자신의 단위수량을 가격으로 설정
        :return: 
        """
        return self.quantity_price * self.quantity

    def is_single_item(self):
        return self.quantity == 1

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
