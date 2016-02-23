import services

from flask import request
from injector import inject
from webapi import app
from webapi.helpers.responses import *


@inject(addressbook=services.AddressBook)
@app.route('/query/endpoints', methods=['GET'])
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


@inject(sparqlcompressor=services.SparqlCompressor, messaging=services.Messenger)
@app.route('/query/<contactid>/sparql')
def outgoing_sparql(sparqlcompressor, messaging, contactid):
    return notimplemented()


@inject(sparqlcompressor=services.SparqlCompressor, messaging=services.Messenger)
@app.route('/query/<contactid>/sparql/update')
def outgoing_sparqlupdate(sparqlcompressor, messaging, contactid):
    return notimplemented()









