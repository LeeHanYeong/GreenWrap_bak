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
    extra = 0


class ProductOptionInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ProductOption
    extra = 0
    show_change_link = True
    template = 'admin/edit_inline/tabular_product_option.html'


class ProductOptionAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ('product', 'title',)
    list_filter = ('product',)
    list_display = ('product', 'title', 'quantity', 'quantity_price', 'price',)
    list_editable = ('title', 'quantity',)
    inlines = [ProductOptionPriceInline]


class ProductOptionPriceAdmin(admin.ModelAdmin):
    pass
