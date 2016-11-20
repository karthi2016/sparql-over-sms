from os import environ
from celery import Celery
from utilities import configmanager

taskqueue_host = configmanager.get_config("taskqueue_host")
if taskqueue_host is None:
    raise Exception("the 'taksqueue_host' configuration is not set.")


celery = Celery('tasks', broker='redis://{0}'.format(taskqueue_host))
celery.conf.CELERY_RESULT_BACKEND = environ.get('CELERY_RESULT_BACKEND', 'redis://{0}'.format(taskqueue_host))
celery.conf.CELERY_EVENT_SERIALIZER = 'pickle'
celery.conf.CELERY_RESULT_SERIALIZER = 'pickle'
celery.conf.CELERY_TASK_SERIALIZER = 'pickle'

from processing.tasks import *
