from rest_framework import viewsets

from ..serializers import ProductCategoryTopSerializer
from ..models import ProductCategoryTop


class ProductCategoryTopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductCategoryTop.objects.all()
    serializer_class = ProductCategoryTopSerializer
