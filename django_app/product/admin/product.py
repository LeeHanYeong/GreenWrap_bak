from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin

from ..models import ProductPrice
from ..admin.product_option import ProductOptionInline

__all__ = (
    'ProductAdmin',
    'ProductPriceAdmin',
)


class ProductPriceInline(admin.TabularInline):
    model = ProductPrice
    # readonly_fields = (
    #     'price',
    #     'start_date',
    # )
    extra = 0
    can_delete = False
    template = 'admin/edit_inline/tabular_non_edit.html'


class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    fieldsets = (
        ('카테고리 정보', {
            'fields': (
                'category',
            )
        }),
        ('기본정보', {
            'fields': (
                'title',
                'short_description',
                'full_description',
                'use_price',
            )
        }),
        ('옵션목록', {
            'fields': (
                'admin_detail_options',
            )
        }),
    )
    readonly_fields = (
        'admin_detail_options',
    )
    list_display = (
        'title',
        'use_price',
        'category',
        'admin_detail_options',
    )
    list_filter = (
        'use_price',
        'category',
        'category__middle_category',
        'category__middle_category__top_category',
    )
    inlines = (
        ProductPriceInline,
        ProductOptionInline,
    )

    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     extra_context = {
    #         'url_price'
    #     }
    #     return super().change_view(request, object_id, form_url=, extra_context)
    # admin_detail_options.short_description = '옵션 목록'
    # admin_detail_options.allow_tags = True


class ProductPriceAdmin(admin.ModelAdmin):
    list_filter = ('product',)
