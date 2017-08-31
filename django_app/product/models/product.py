from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from utils.exceptions import NotAllowedSelfPrice, PriceDoesNotExist, PriceError
from utils.fields import DefaultStaticImageField
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
    PRODUCT_TYPE_VINYL = 'vinyl'
    CHOICES_PRODUCT_TYPES = (
        (PRODUCT_TYPE_VINYL, '비닐'),
    )

    product_type = models.CharField(
        '상품 타입', choices=CHOICES_PRODUCT_TYPES, max_length=15, blank=True)
    category = models.ForeignKey(
        ProductCategorySmall,
        verbose_name='카테고리',
        related_name='product_set',
    )
    title = models.CharField('상품명', max_length=60, blank=True)
    size = models.CharField('사이즈', max_length=50, blank=True)
    use_size_as_title = models.BooleanField('사이즈를 상품명으로 사용', default=False)
    add_small_category_to_title = models.BooleanField('상품명 앞에 소분류명을 추가', default=False)
    add_middle_category_to_title = models.BooleanField('상품명 앞에 중분류명을 추가', default=False)
    add_size_to_title = models.BooleanField('상품명 뒤에 사이즈를 추가', default=False)

    short_description = models.CharField('짧은 설명', max_length=60, blank=True)
    full_description = models.TextField('상세 설명', blank=True)
    use_price = models.BooleanField('자체 가격 사용 여부 (옵션 없음)', default=False)

    class Meta(SortableMixin.Meta):
        verbose_name = '상품'
        verbose_name_plural = '%s 목록' % verbose_name

    # Model methods
    def __str__(self):
        title = self.title
        if self.use_size_as_title:
            title = self.size
        if self.add_small_category_to_title:
            title = '{small_category} {title}'.format(
                small_category=self.category.title,
                title=title
            )
        if self.add_middle_category_to_title:
            title = '{middle_category} {title}'.format(
                middle_category=self.category.middle_category.title,
                title=title
            )
        if self.add_size_to_title:
            title = '{title} {size}'.format(
                title=title,
                size=self.size
            )
        if self.use_price:
            return '{title} ({price:,d}원)'.format(
                title=title,
                price=self.price,
            )
        return title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # OTO ProductInfo존재시 product_type설정
        self.save_product_info(*args, **kwargs)
        # 가격목록 없을경우 생성
        if not self.price_set.exists():
            self.price_set.create()

    def clean(self):
        if self.use_price and not self.price_set.exists():
            raise ValidationError('가격 사용 여부는 연결된 상품 가격 항목이 있을 때만 활성화 할 수 있습니다')

    # Model methods helper
    def save_product_info(self, *args, **kwargs):
        if hasattr(self, 'vinylinfo'):
            self.product_type = self.PRODUCT_TYPE_VINYL
            super().save(*args, **kwargs)

    # Properties
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

    @property
    def info(self):
        if self.product_type == self.PRODUCT_TYPE_VINYL and hasattr(self, 'vinylinfo'):
            return self.vinylinfo
        return None

    # Custom methods
    # Admin functions
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


class ProductImage(Model):
    product = models.ForeignKey(Product)
    img = DefaultStaticImageField(
        upload_to='product',
        blank=True
    )

    def __str__(self):
        return '상품({}) 이미지'.format(
            self.product.__str__()
        )


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
