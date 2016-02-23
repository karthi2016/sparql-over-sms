import services

from flask import request
from injector import inject
from services.messenger import SPARQL_QUERY, SPARQL_UPDATE
from webapi import app
from webapi.helpers.crossdomain import crossdomain
from webapi.helpers.responses import *


@crossdomain()
@inject(addressbook=services.AddressBook)
@app.route('/query/endpoints', methods=['GET', 'OPTIONS'])
def get_queryendpoints(addressbook):
    contacts = [c for c in addressbook.get_contacts() if c['sparqlenabled'] == 'yes']

    endpoints = []
    for contact in contacts:
        endpoint = {
            'contact': contact['fullname'],
            'sparql': {
                'query': '/query/{0}/sparql'.format(contact['contactid']),
                'update': '/query/{0}/sparql/update'.format(contact['contactid'])
            }
        }
        endpoints.append(endpoint)

    return ok(endpoints)


@crossdomain()
@inject(sparqlprocessor=services.SparqlProcessor, messenger=services.Messenger)
@app.route('/query/<contactid>/sparql', methods=['GET', 'OPTIONS'])
def outgoing_sparql(sparqlprocessor, messenger, contactid):
    query = request.args.get('query')

    # send query (packed) to contact
    packed = sparqlprocessor.pack(query)
    messenger.send(contactid, SPARQL_QUERY, packed)

    return accepted()


@crossdomain()
@inject(sparqlprocessor=services.SparqlProcessor, messenger=services.Messenger)
@app.route('/query/<contactid>/sparql/update', methods=['POST', 'OPTIONS'])
def outgoing_sparqlupdate(sparqlprocessor, messenger, contactid):
    update = request.form.get('update')

    # send update (packed) to contact
    packed = sparqlprocessor.pack(update)
    messenger.send(contactid, SPARQL_UPDATE, packed)

    return accepted()









