from webapi import app
from webapi.helpers.responses import *


@app.route('/messages')
def get_messages(repository):
    messages = repository.get_messages()

    # return messages as JSON
    return ok('[{}]'.format(','.join([m.as_json() for m in messages])), 'application/json')


@app.route('/message/<identifier>')
def get_message_byid(repository, identifier):
    message = repository.get_message_byid(identifier)

    if message is None:
        return notfound()

    # return message as JSON
    return ok(message.as_json(), 'application/json')
