from django.contrib import admin

from ..models import *
from .product import *
from .product_category import *
from .product_option import *

admin.site.register(ProductCategoryTop, ProductCategoryTopAdmin)
admin.site.register(ProductCategoryMiddle, ProductCategoryMiddleAdmin)
admin.site.register(ProductCategorySmall)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPrice, ProductPriceAdmin)
admin.site.register(ProductOption, ProductOptionAdmin)
admin.site.register(ProductOptionPrice, ProductOptionPriceAdmin)