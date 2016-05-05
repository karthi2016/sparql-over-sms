import repositories
from flask import request

from injector import inject
from webapi import app
from webapi.helpers.responses import *


@app.route('/contacts')
@inject(repository=repositories.ContactRepo)
def get_contacts(repository):
    contacts = repository.get_contacts()

    # return contacts as JSON
    return ok('[{}]'.format(','.join([c.as_json() for c in contacts])), 'application/json')


@app.route('/contact/<identifier>')
@inject(repository=repositories.ContactRepo)
def get_contact_byid(repository, identifier):
    contact = repository.get_contact_byid(identifier)

    if contact is None:
        return notfound()

    # return contact as JSON
    return ok(contact.as_json(), 'application/json')

@app.route('/contacts', methods=['POST'])
@inject(repository=repositories.ContactRepo)
def add_contact(repository):
    payload = request.get_json()

    # unpack payload
    identifier = payload['identifier']
    name = payload['name']
    phonenumber = payload['phonenumber']
    ip = payload.get('ip', None)

    repository.add_contact(identifier, name, phonenumber, ip)
    return nocontent()

@app.route('/contact/<identifier>', methods=['PUT'])
@inject(repository=repositories.ContactRepo)
def update_contact(repository, identifier):
    payload = request.get_json()

    # unpack payload
    name = payload['name']
    phonenumber = payload['phonenumber']
    ip = payload.get('ip', None)

    repository.update_contact(identifier, name, phonenumber, ip)
    return nocontent()

@app.route('/contact/<identifier>', methods=['DELETE'])
@inject(repository=repositories.ContactRepo)
def delete_contact(repository, identifier):
    repository.delete_contact(identifier)
    return nocontent()





