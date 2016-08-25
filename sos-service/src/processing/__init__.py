from os import environ
from celery import Celery

celery = Celery('tasks', broker='amqp://guest@127.0.0.1//')
celery.conf.CELERY_RESULT_BACKEND = environ.get('CELERY_RESULT_BACKEND', 'amqp')

from processing.tasks import *
