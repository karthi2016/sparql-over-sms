import services

from base64 import b64decode
from flask import request
from injector import inject
from services.messenger import SPARQL_QUERY
from webapi import app
from webapi.helpers.responses import *


@inject(messenger=services.Messenger, sparqlprocessor=services.SparqlProcessor)
@app.route('/incoming', methods=['POST'])
def incoming(messenger, sparqlprocessor):
    payload = request.get_json()
    sender = payload['sender']
    body = b64decode(payload['body']).decode('utf-8')

    # process message
    message = messenger.receive(sender, body)
    if message['category'] == SPARQL_QUERY:
        print(sparqlprocessor.unpack(message['body']))

    return accepted()
