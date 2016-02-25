import pipelines
import services

from flask import request
from injector import inject
from pipelines.wrappers.message import Message
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
@inject(pipeline=pipelines.SendSparqlQuery)
@app.route('/query/<contactid>/sparql', methods=['GET', 'OPTIONS'])
def outgoing_sparql(pipeline, contactid):
    query = request.args.get('query')

    # send sparql query to contact
    message = Message(SPARQL_QUERY, query, receiver=contactid)
    result = pipeline.handle(message)

    print(result)
    return accepted()


@crossdomain()
@inject(pipeline=pipelines.SendSparqlUpdate)
@app.route('/query/<contactid>/sparql/update', methods=['POST', 'OPTIONS'])
def outgoing_sparqlupdate(pipeline, contactid):
    update = request.form.get('update')

    # send sparql update to contact
    message = Message(SPARQL_UPDATE, update, receiver=contactid)
    result = pipeline.handle(message)

    print(result)
    return accepted()









