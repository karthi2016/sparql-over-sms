from os import environ
from celery import Celery


celery = Celery('tasks', broker='redis://sos-taskqueue')
celery.conf.CELERY_RESULT_BACKEND = environ.get('CELERY_RESULT_BACKEND', 'redis://sos-taskqueue')

from processing.tasks import *
