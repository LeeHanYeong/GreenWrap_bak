from rest_framework import viewsets, filters

from ..models import Product
from ..serializers import ProductListSerializer, ProductDetailSerializer

__all__ = (
    'ProductViewSet',
)


# class ProductViewSet(viewsets.ReadOnlyModelViewSet):
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('category', 'category__middle_category')

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductListSerializer
