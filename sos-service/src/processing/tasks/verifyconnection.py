from time import time
from processing import celery


@celery.task
def verify_connection(past_timestamp):
    return round(time() - past_timestamp)
