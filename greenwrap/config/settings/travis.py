# deploy.py
from .base import *

DEBUG = False
config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())
config_secret_travis = json.loads(open(CONFIG_SECRET_TRAVIS_FILE).read())

# WSGI application
WSGI_APPLICATION = 'config.wsgi.travis.application'

# AWS settings
AWS_ACCESS_KEY_ID = config_secret_deploy['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config_secret_deploy['aws']['secret_access_key']
AWS_STORAGE_BUCKET_NAME = config_secret_deploy['aws']['s3_bucket_name']
AWS_S3_REGION_NAME = config_secret_deploy['aws']['s3_region_name']
S3_USE_SIGV4 = True

# Storage settings
STATICFILES_LOCATION = 'travis_static'
MEDIAFILES_LOCATION = 'travis_media'
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'

# Static URLs
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Database
DATABASES = config_secret_travis['django']['databases']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': [
                'console',
            ],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}
