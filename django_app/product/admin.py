from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from product.models import *


class ProductCategoryTopAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


class ProductCategoryMiddleAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_filter = ('top_category',)


class ProductAdmin(admin.ModelAdmin):
    pass


class ProductPriceAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductCategoryTop, ProductCategoryTopAdmin)
admin.site.register(ProductCategoryMiddle, ProductCategoryMiddleAdmin)
admin.site.register(ProductCategorySmall)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPrice, ProductPriceAdmin)
