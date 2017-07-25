from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

__all__ = (
    'ProductCategoryTopAdmin',
    'ProductCategoryMiddleAdmin',
    'ProductCategorySmallAdmin',
)


class ProductCategoryTopAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


class ProductCategoryMiddleAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_filter = ('top_category',)


class ProductCategorySmallAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_filter = ('middle_category',)
