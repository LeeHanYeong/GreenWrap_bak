from rest_framework import viewsets
from ..models import Product

__all__ = (
    'ProductViewSet',
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        print(self.action)
