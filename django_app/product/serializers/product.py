from rest_framework import serializers

from ..models.product import Product

__all__ = (
    'ProductListSerializer',
    'ProductDetailSerializer',
)


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'title',
            'short_description',
            'use_price',
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta(ProductListSerializer.Meta):
        model = Product
        fields = (
            'title',
            'short_description',
            'full_description',
            'use_price',
        )
