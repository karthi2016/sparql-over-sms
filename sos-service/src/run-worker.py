#!/usr/bin/python
from celery import Celery 

jobqueue = Celery()

if __name__ == "__main__":
    argv = [
        'worker',
        '--app=processing',
        '--loglevel=DEBUG',
    ]
    jobqueue.worker_main(argv)
