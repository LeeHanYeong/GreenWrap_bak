from django.db import models
from django.utils import timezone

from .product import Product
from utils.models import Model, BasePrice

__all__ = (
    'ProductFeature',
    'ProductFeaturePrice',
)


class ProductFeature(Model):
    """
    상품 특징
        하나의 상품이 특징에 따라 여러 상품으로 나누어지는 단위
        Product와 MTO으로 매칭
            ex) 6mm, 8mm...등
    """
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=100)

    def __str__(self):
        return '{product} Feature ({title})'.format(
            product=self.product.title,
            title=self.title,
        )


class ProductFeaturePrice(BasePrice):
    product_feature = models.ForeignKey(Product, related_name='product_feature_price_set')

    def __str__(self):
        return '상품 특징({}) 가격정보: {}'.format(
            self.product.title,
            super().__str__()
        )