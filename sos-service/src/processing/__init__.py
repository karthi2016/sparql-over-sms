from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost//')

from processing.tasks import *
