import services

from base64 import b64decode
from flask import request
from injector import inject
from services.messenger import SPARQL_QUERY
from SPARQLWrapper import SPARQLWrapper
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
        sparql = SPARQLWrapper(app.config['c_triplestore']['endpoints']['query'])
        query = sparqlprocessor.unpack(message['body'])

        sparql.returnFormat = 'json'
        sparql.setQuery(query)
        print(sparql.query().convert())

    return accepted()
