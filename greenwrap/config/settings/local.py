# debug.py
from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

# INSTALLED_APPS
INSTALLED_APPS.append('django_extensions')

# WSGI application
WSGI_APPLICATION = 'config.wsgi.debug.application'

# Static URLs
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')

# 디버그모드니까 DEBUG는 True
DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Celery
CELERY_BROKER_URL = '{}:{}'.format(
    config_secret_debug['django']['celery']['broker_url'],
    config_secret_debug['django']['celery']['broker_port']
)
CELERY_RESULT_BACKEND = '{}:{}'.format(
    config_secret_debug['django']['celery']['broker_url'],
    config_secret_debug['django']['celery']['broker_port']
)
