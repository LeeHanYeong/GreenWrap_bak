from django.db import models
from django.utils import timezone

from utils.models import Model, BasePrice
from .product_category import ProductCategorySmall

__all__ = (
    'Product',
    'ProductPrice',
)


class Product(Model):
    """
    상품
    """
    category = models.ForeignKey(ProductCategorySmall, verbose_name='카테고리')
    title = models.CharField('상품명', max_length=60)
    short_description = models.CharField('짧은 설명', max_length=60, blank=True)
    full_description = models.TextField('상세 설명', blank=True)
    use_price = models.BooleanField('가격 사용 여부', default=False)

    class Meta:
        verbose_name = '상품'
        verbose_name_plural = '%s 목록' % verbose_name

    def __str__(self):
        if self.use_price:
            return '{title} ({price:,d}원)'.format(
                title=self.title,
                price=0
            )
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.use_price and not self.product_price_set.exists():
            self.use_price = False
            super().save(*args, **kwargs)


class ProductPrice(BasePrice):
    product = models.ForeignKey(Product, related_name='product_price_set')

    class Meta:
        verbose_name = '상품 가격'
        verbose_name_plural = '%s 목록' % verbose_name

    def __str__(self):
        return '상품({}) 가격정보: {}'.format(
            self.product.title,
            super().__str__()
        )
