FROM python:3.8

RUN pip install -U pip
RUN pip install Flask
RUN pip install uwsgi
RUN pip install redis
RUN pip install celery

CMD uwsgi uwsgi.ini

RUN useradd -r web
USER web
WORKDIR /var/www