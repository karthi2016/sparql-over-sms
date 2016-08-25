from processing import celery


@celery.task
def process_outgoingmessage(messageid):
    print('needs to send {0}'.format(messageid))
