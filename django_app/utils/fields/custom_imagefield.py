from django.conf import settings
from django.db.models.fields.files import ImageFieldFile, ImageField
from django.utils.module_loading import import_string

__all__ = (
    'DefaultStaticImageField',
)


class DefaultStaticImageFieldFile(ImageFieldFile):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 1. static_image_path가 지정되어 있으며
        # 2. self.name이 존재하지 않거나 해당 name이 static_image_path인경우
        # -> 에는 storage를 STATICFILES_STORAGE를 사용하며, name은 static_image_path값을 사용한다
        if self.field.static_image_path and (
                    not self.name or self.name == self.field.static_image_path):
            self.name = self.field.static_image_path
            self.storage = import_string(settings.STATICFILES_STORAGE)()


class DefaultStaticImageField(ImageField):
    attr_class = DefaultStaticImageFieldFile

    def __init__(self, *args, **kwargs):
        self.static_image_path = kwargs.pop('default_static_image', 'images/no_image.png')
        super().__init__(*args, **kwargs)
