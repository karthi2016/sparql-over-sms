import services

from base64 import b64decode
from flask import request
from injector import inject
from pipelines.receivesparqlquery import ReceiveSparqlQuery
from pipelines.receivesparqlupdate import ReceiveSparqlUpdate
from pipelines.wrappers.message import Message
from services.messenger import SPARQL_QUERY, Messenger, SPARQL_UPDATE
from SPARQLWrapper import SPARQLWrapper
from webapi import app
from webapi.helpers.responses import *


@inject(addressbook=services.AddressBook)
@app.route('/incoming', methods=['POST'])
def incoming(addressbook):
    payload = request.get_json()
    phonenumber = payload['sender']
    content = b64decode(payload['body']).decode('utf-8').strip()

    # process message
    categoryid, body = content.split(' ', 1)
    sender = addressbook.find_contact(phonenumber)
    category = {'{0}'.format(value): key for key, value in Messenger.categories.items()}[categoryid]

    message = Message(category, body, sender=sender['contactid'])
    pipeline = None
    if category is SPARQL_QUERY:
        pipeline = ReceiveSparqlQuery()
    elif category is SPARQL_UPDATE:
        pipeline = ReceiveSparqlUpdate()

    if pipeline is not None:
        result = pipeline.handle(message)
        print(result)
    else:
        print('No suitable pipeline found..')

    return accepted()
