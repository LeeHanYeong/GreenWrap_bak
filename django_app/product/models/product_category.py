from django.db import models

from utils.mixins import SortableMixin
from utils.models import Model

__all__ = (
    'ProductCategoryTop',
    'ProductCategoryMiddle',
    'ProductCategorySmall',
)


class ProductCategoryTop(SortableMixin, Model):
    title = models.CharField('카테고리명', max_length=50)

    class Meta(SortableMixin.Meta):
        verbose_name = '최상위 카테고리'
        verbose_name_plural = '%s 목록' % verbose_name

    def __str__(self):
        return '{}'.format(
            self.title
        )


class ProductCategoryMiddle(Model):
    top_category = models.ForeignKey(
        ProductCategoryTop,
        verbose_name='최상위 카테고리',
        related_name='sub_category_set',
    )
    title = models.CharField('중분류명', max_length=50)

    class Meta:
        verbose_name = '중분류'
        verbose_name_plural = '%s 목록' % verbose_name
        order_with_respect_to = 'top_category'

    def __str__(self):
        return '{} > {}'.format(
            self.top_category.title,
            self.title
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.sub_category_set.exists():
            ProductCategorySmall.objects.create(
                middle_category=self,
            )


class ProductCategorySmall(Model):
    middle_category = models.ForeignKey(
        ProductCategoryMiddle,
        verbose_name='중분류',
        related_name='sub_category_set',
    )
    title = models.CharField('소분류명', max_length=50, default='미분류')

    class Meta:
        verbose_name = '소분류'
        verbose_name_plural = '%s 목록' % verbose_name
        order_with_respect_to = 'middle_category'

    def __str__(self):
        return '{} > {} > {}'.format(
            self.middle_category.top_category.title,
            self.middle_category.title,
            self.title
        )
