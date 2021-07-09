FROM python:3.8

RUN pip install -U pip
RUN pip install celery
RUN pip install redis

CMD celery -A tasks worker --loglevel=info --autoscale=10,3

RUN useradd -r celery
USER celery
WORKDIR /var/tasks