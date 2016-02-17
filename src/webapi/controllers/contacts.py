import json
import services

from injector import inject
from webapi import app
from flask import Response, request


@inject(addressbook=services.AddressBook)
@app.route('/contacts', methods=['GET'])
def retreive_contacts(addressbook):
    contacts = addressbook.get_contacts()

    return Response(json.dumps(contacts), mimetype='application/json')


@inject(addressbook=services.AddressBook)
@app.route('/contact/<contactid>', methods=['GET'])
def retreive_contact(contactid, addressbook):
    contact = addressbook.get_contact(contactid)

    return Response(json.dumps(contact), mimetype='application/json')


@inject(addressbook=services.AddressBook)
@app.route('/contacts', methods=['POST'])
def create_contact(addressbook):
    contactinfo = request.get_json()
    addressbook.add_contact(contactinfo)

    return Response(status=201)


@inject(addressbook=services.AddressBook)
@app.route('/contact/<contactid>', methods=['PUT'])
def update_contact(contactid, addressbook):
    contactinfo = request.get_json()
    addressbook.update_contact(contactid, contactinfo)

    return Response(status=204)


@inject(addressbook=services.AddressBook)
@app.route('/contact/<contactid>', methods=['DELETE'])
def delete_contact(contactid, addressbook):
    addressbook.remove_contact(contactid)

    return Response(status=204)

