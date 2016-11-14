from os import environ
from celery import Celery


celery = Celery('tasks', broker='redis://localhost')
celery.conf.CELERY_RESULT_BACKEND = environ.get('CELERY_RESULT_BACKEND', 'redis')

from processing.tasks import *
