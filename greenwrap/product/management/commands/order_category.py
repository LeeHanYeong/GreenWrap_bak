from django.core.management.base import BaseCommand

from ...models import ProductCategoryTop, ProductCategoryMiddle, ProductCategorySmall


def order_category():
    for top_index, top_category in enumerate(ProductCategoryTop.objects.iterator()):
        # 중분류의 순서를 정렬
        # print('중분류 순서 정렬')
        for middle_index, middle_category in enumerate(
                top_category.sub_category_set.iterator()):
            # middle_category.update(_order=top_index * 10 + middle_index)
            ProductCategoryMiddle.objects.filter(pk=middle_category.pk).update(_order=top_index * 10 + middle_index)
            print(' {}'.format(
                middle_category.title
            ))

            # 해당 중분류의 소분류 순서를 정렬
            # print('  소분류 순서 정렬')
            for small_index, small_category in enumerate(
                    middle_category.sub_category_set.iterator()):
                # small_category.update(_order=top_index * 100 + middle_index * 10 + small_index)
                ProductCategorySmall.objects.filter(pk=small_category.pk).update(_order=top_index * 100 + middle_index * 10 + small_index)
                print('   {}'.format(
                    small_category.title
                ))
        print('')


class Command(BaseCommand):
    def handle(self, *args, **options):
        order_category()
