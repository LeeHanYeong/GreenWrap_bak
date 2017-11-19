import collections
import os

from collections import Iterable

ROOT_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def combine_dict(origin, update):
    for key, value in update.items():
        if isinstance(value, collections.Mapping):
            origin[key] = combine_dict(origin.get(key, {}), value)
        else:
            origin[key] = update[key]
    return origin


def get_logging_dict(log_dir, app_names):
    def __get_file_handler(app_name, level):
        return {
            'level': level.upper(),
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_dir, f'{app_name}_{level}.log'),
            # Limit 10MB x 10
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 10,
        }

    def __get_logger(app_name, levels=None):
        if not levels:
            levels = ['debug', 'error']
        return {
            'handlers': [f'file_{app_name}_{level}' for level in levels],
            'level': 'DEBUG',
            'propagate': True,
        }

    def _get_file_handlers(app_names, levels=None):
        if not levels:
            levels = ['debug', 'error']
        handlers = {}
        for level in levels:
            handlers.update(
                {f'file_{app_name}_{level}': __get_file_handler(app_name, level=level)
                 for app_name in app_names})
        return handlers

    def _get_loggers(app_names, levels=None):
        return {app_name: __get_logger(app_name, levels=levels) for app_name in app_names}

    logging_dict = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': _get_file_handlers(app_names),
        'loggers': _get_loggers(app_names),
    }
    return logging_dict


def set_dependent_settings(module, config):
    def convert_paths(obj):
        def _convert(path):
            if path.startswith('os.path'):
                return eval(path)
            return path

        if isinstance(obj, str):
            return _convert(obj)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                if isinstance(item, Iterable):
                    obj[index] = convert_paths(item)
                elif isinstance(item, str):
                    obj[index] = _convert(item)
        elif isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, Iterable):
                    obj[key] = convert_paths(value)
                elif isinstance(value, str):
                    obj[key] = _convert(value)
        return obj

    databases = convert_paths(config['django'].get('databases'))
    media_root = convert_paths(config['django'].get('media_root'))
    log_dir = convert_paths(config['django'].get('log_dir'))
    email_config = config['django'].get('email')

    settings = {}
    if databases:
        settings['DATABASES'] = databases
    if media_root:
        settings['MEDIA_ROOT'] = media_root
    if log_dir:
        settings['LOGGING'] = get_logging_dict(log_dir, ['hitomi', 'bam', 'tumblr'])
    if email_config:
        settings['EMAIL_HOST'] = email_config['host']
        settings['EMAIL_PORT'] = email_config['port']
        settings['EMAIL_HOST_USER'] = email_config['host_user']
        settings['EMAIL_HOST_PASSWORD'] = email_config['host_password']
        settings['EMAIL_USE_TLS'] = email_config['use_tls']
        settings['EMAIL_DEFAULT_FROM_EMAIL'] = email_config['default_from_email']
        settings['EMAIL_BACKEND'] = 'django.core.mail.backends.smtp.EmailBackend'
    for key, value in settings.items():
        setattr(module, key, value)
