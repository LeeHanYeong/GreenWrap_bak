from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin

from ..models import ProductOptionPrice, ProductOption

__all__ = (
    'ProductOptionInline',
    'ProductOptionAdmin',
    'ProductOptionPriceAdmin',
)


class ProductOptionPriceInline(admin.TabularInline):
    model = ProductOptionPrice
    extra = 1


class ProductOptionInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ProductOption
    extra = 1


class ProductOptionAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [ProductOptionPriceInline]


class ProductOptionPriceAdmin(admin.ModelAdmin):
    pass
