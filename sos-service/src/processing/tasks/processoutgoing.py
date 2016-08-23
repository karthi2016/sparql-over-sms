from processing import app


@app.task
def process_outgoingmessage(messageid):
    print('needs to send {0}'.format(messageid))
