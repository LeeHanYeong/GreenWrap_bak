from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone

from utils.exceptions import NotAllowedSelfPrice, PriceDoesNotExist, PriceError
from utils.mixins import SortableMixin
from utils.models import Model, BasePrice
from .product_category import ProductCategorySmall

__all__ = (
    'Product',
    'ProductPrice',
)


class Product(SortableMixin, Model):
    """
    상품
    """
    category = models.ForeignKey(
        ProductCategorySmall,
        verbose_name='카테고리',
        related_name='product_set',
    )
    title = models.CharField('상품명', max_length=60)
    short_description = models.CharField('짧은 설명', max_length=60, blank=True)
    full_description = models.TextField('상세 설명', blank=True)
    use_price = models.BooleanField('가격 사용 여부', default=False)

    class Meta(SortableMixin.Meta):
        verbose_name = '상품'
        verbose_name_plural = '%s 목록' % verbose_name

    def __str__(self):
        if self.use_price:
            return '{title} ({price:,d}원)'.format(
                title=self.title,
                price=self.price,
            )
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.price_set.exists():
            self.price_set.create()

    def clean(self):
        if self.use_price and not self.price_set.exists():
            raise ValidationError('가격 사용 여부는 연결된 상품 가격 항목이 있을 때만 활성화 할 수 있습니다')

    @property
    def price(self):
        if not self.use_price:
            raise NotAllowedSelfPrice(self)
        elif not self.price_set.exists():
            try:
                self.save()
            except:
                raise PriceDoesNotExist(self)
        try:
            return self.price_set.first().price
        except Exception as e:
            raise PriceError(self, e)

    def admin_detail_options(self):
        ret = ''
        for option in self.option_set.iterator():
            ret += '<a href="{}">{} [{:,d}원]</a><br>'.format(
                reverse(
                    'admin:product_productoption_change',
                    args=(option.pk,)),
                option.title,
                option.price
            )
        return ret

    admin_detail_options.short_description = '옵션 목록'
    admin_detail_options.allow_tags = True


class ProductPrice(BasePrice):
    product = models.ForeignKey(
        Product,
        verbose_name='상품 가격',
        related_name='price_set'
    )

    class Meta(BasePrice.Meta):
        verbose_name = '상품 가격'
        verbose_name_plural = '%s 목록' % verbose_name

    def __str__(self):
        return '상품({}) 가격: {}'.format(
            self.product.title,
            super().__str__()
        )
