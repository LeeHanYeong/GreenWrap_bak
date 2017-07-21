from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

__all__ = (
    'ProductCategoryTopAdmin',
    'ProductCategoryMiddleAdmin',
)


class ProductCategoryTopAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


class ProductCategoryMiddleAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_filter = ('top_category',)
