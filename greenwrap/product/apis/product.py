from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from ..models import Product
from ..serializers import ProductListSerializer, ProductDetailSerializer

__all__ = (
    'ProductViewSet',
)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category', 'category__middle_category')

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductListSerializer
