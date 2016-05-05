from flask import request
from persistence.repositories import ContactRepo
from webapi import app
from webapi.helpers.responses import *


@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = ContactRepo.get_contacts()

    # return contacts as JSON
    return ok([c.as_dict() for c in contacts], 'application/json')


@app.route('/contact/<identifier>', methods=['GET'])
def get_contact_byid(identifier):
    contact = ContactRepo.get_contact_byid(identifier)

    if contact is None:
        return notfound()

    # return contact as JSON
    return ok(contact.as_dict(), 'application/json')

@app.route('/contacts', methods=['POST'])
def add_contact():
    payload = request.get_json()

    # unpack payload
    identifier = payload['identifier']
    name = payload['name']
    phonenumber = payload.get('phonenumber', None)
    ip = payload.get('ip', None)

    ContactRepo.add_contact(identifier, name, phonenumber, ip)
    return nocontent()

@app.route('/contact/<identifier>', methods=['PUT'])
def update_contact(identifier):
    payload = request.get_json()

    # unpack payload
    name = payload['name']
    phonenumber = payload.get('phonenumber', None)
    ip = payload.get('ip', None)

    ContactRepo.update_contact(identifier, name, phonenumber, ip)
    return nocontent()

@app.route('/contact/<identifier>', methods=['DELETE'])
def delete_contact(identifier):
    ContactRepo.delete_contact(identifier)
    return nocontent()





