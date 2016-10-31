from os import environ
from celery import Celery


celery = Celery('tasks', broker='redis://localhost:32789')
celery.conf.CELERY_RESULT_BACKEND = environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:32789')

from processing.tasks import *
