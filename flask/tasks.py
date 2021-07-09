# tasks.py
from celery import Celery

BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
app = Celery('tasks', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)

@app.task
def add(x, y):
        pass
