from .product import *
from .product_category import *
from .product_info import *
from .product_option import *
from ..models import *

admin.site.register(ProductCategoryTop, ProductCategoryTopAdmin)
admin.site.register(ProductCategoryMiddle, ProductCategoryMiddleAdmin)
admin.site.register(ProductCategorySmall, ProductCategorySmallAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPrice, ProductPriceAdmin)
admin.site.register(ProductOption, ProductOptionAdmin)
admin.site.register(ProductOptionPrice, ProductOptionPriceAdmin)

admin.site.register(VinylInfo, VinylInfoAdmin)
