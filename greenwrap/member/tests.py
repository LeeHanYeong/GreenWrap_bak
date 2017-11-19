from django.conf import settings
from django.contrib.auth import get_user_model, authenticate
from django.core.management import call_command
from django.test import TestCase

User = get_user_model()


class CommandTest(TestCase):
    def test_createsu(self):
        args = []
        options = {}
        call_command('createsu', *args, **options)
        user = authenticate(
            username=settings.DEFAULT_SUPERUSER_USERNAME,
            email=settings.DEFAULT_SUPERUSER_EMAIL,
            password=settings.DEFAULT_SUPERUSER_PASSWORD,
        )
        self.assertIsNotNone(user)
