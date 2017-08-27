from django.db import models

from utils.models import Model

__all__ = (
    'ProductInfo',
    'VinylInfo',
)


class ProductInfo(Model):
    product = models.OneToOneField('Product', verbose_name='상품')

    class Meta:
        abstract = True


class VinylInfo(ProductInfo):
    thickness = models.DecimalField('두께', max_digits=6, decimal_places=3, blank=True, null=True)
    material = models.CharField('재질', max_length=60, blank=True)

    class Meta:
        verbose_name = '상품정보 - 비닐'
        verbose_name_plural = '%s 목록' % verbose_name

    def __str__(self):
        return '{product} 정보 (두께: {thickness}, 재질: {material})'.format(
            product=self.product.__str__(),
            thickness=self.thickness,
            material=self.material
        )
