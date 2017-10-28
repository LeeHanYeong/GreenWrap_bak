from rest_framework import serializers

from ..models.product import Product

__all__ = (
    'ProductListSerializer',
    'ProductDetailSerializer',
)


class ProductListSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='__str__')
    product_type_display = serializers.CharField(source='get_product_type_display')

    class Meta:
        model = Product
        fields = (
            'pk',
            'title',
            'product_type',
            'product_type_display',
            'short_description',
            'use_price',
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # use_price가 True일 경우 price정보 추가
        if instance.use_price:
            ret['price'] = instance.price
        # OTO로 연결된 ProductInfo정보를 rep에 update
        if instance.info and instance.info.serializer_class:
            ret.update(instance.info.serializer_class(instance.info).data)
        return ret


class ProductDetailSerializer(ProductListSerializer):
    class Meta(ProductListSerializer.Meta):
        model = Product
        fields = ProductListSerializer.Meta.fields + (
            'full_description',
            'use_price',
        )
