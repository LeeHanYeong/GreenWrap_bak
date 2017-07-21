from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin

from ..models import ProductPrice

__all__ = (
    'ProductAdmin',
    'ProductPriceAdmin',
)


class ProductPriceInline(admin.TabularInline):
    model = ProductPrice
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductPriceInline,)


class ProductPriceAdmin(admin.ModelAdmin):
    pass
