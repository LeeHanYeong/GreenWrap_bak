# debug.py
from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

# INSTALLED_APPS
INSTALLED_APPS.append('django_extensions')

# WSGI application
WSGI_APPLICATION = 'config.wsgi.debug.application'

# AWS settings
AWS_ACCESS_KEY_ID = config_secret_debug['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config_secret_debug['aws']['secret_access_key']
AWS_STORAGE_BUCKET_NAME = config_secret_debug['aws']['s3_bucket_name']
AWS_S3_REGION_NAME = config_secret_debug['aws']['s3_region_name']
S3_USE_SIGV4 = True

# Storage settings
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'

# Static URLs
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# 디버그모드니까 DEBUG는 True
DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']

# Database
DATABASES = config_secret_debug['django']['databases']

# Celery
CELERY_BROKER_URL = '{}:{}'.format(
    config_secret_debug['django']['celery']['broker_url'],
    config_secret_debug['django']['celery']['broker_port']
)
CELERY_RESULT_BACKEND = '{}:{}'.format(
    config_secret_debug['django']['celery']['broker_url'],
    config_secret_debug['django']['celery']['broker_port']
)
