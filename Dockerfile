FROM        d.lhy.kr/greenwrap
MAINTAINER  dev@azelf.com

# DJANGO_SETTINGS_MODULE설정
COPY        . /srv/app
WORKDIR     /srv/app/django_app
CMD         supervisord -n
EXPOSE      80 8000