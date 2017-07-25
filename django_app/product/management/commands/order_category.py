from django.core.management.base import BaseCommand

from ...models import ProductCategoryTop


class Command(BaseCommand):
    def handle(self, *args, **options):
        for top_index, top_category in enumerate(ProductCategoryTop.objects.iterator()):
            # 중분류의 순서를 정렬
            # self.stdout.write('중분류 순서 정렬')
            for middle_index, middle_category in enumerate(
                    top_category.sub_category_set.iterator()):
                middle_category._order = top_index * 10 + middle_index
                middle_category.save()
                self.stdout.write(' {}'.format(
                    middle_category.title
                ))

                # 해당 중분류의 소분류 순서를 정렬
                # self.stdout.write('  소분류 순서 정렬')
                for small_index, small_category in enumerate(
                        middle_category.sub_category_set.iterator()):
                    small_category._order = small_index * 10 + small_index
                    small_category.save()
                    self.stdout.write('   {}'.format(
                        small_category.title
                    ))
            self.stdout.write('')