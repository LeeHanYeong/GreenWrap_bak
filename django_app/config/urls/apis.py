from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from product.apis import ProductViewSet, ProductCategoryTopViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'product/category/top', ProductCategoryTopViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
