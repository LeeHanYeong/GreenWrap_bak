from rest_framework import serializers

from ..models import ProductCategoryTop, ProductCategorySmall, ProductCategoryMiddle

__all__ = (
    'ProductCategorySmallSerializer',
    'ProductCategoryMiddleSerializer',
    'ProductCategoryTopSerializer',
)


class ProductCategorySmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategorySmall
        fields = (
            'pk',
            'title',
        )


class ProductCategoryMiddleSerializer(serializers.ModelSerializer):
    sub_category_set = ProductCategorySmallSerializer(many=True)

    class Meta:
        model = ProductCategoryMiddle
        fields = (
            'pk',
            'title',
            'sub_category_set',
        )


class ProductCategoryTopSerializer(serializers.ModelSerializer):
    sub_category_set = ProductCategoryMiddleSerializer(many=True)

    class Meta:
        model = ProductCategoryTop
        fields = (
            'pk',
            'title',
            'sub_category_set',
        )
