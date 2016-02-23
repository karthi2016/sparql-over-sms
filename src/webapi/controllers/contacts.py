import services

from flask import request
from injector import inject
from webapi import app
from webapi.helpers.responses import *


@inject(addressbook=services.AddressBook)
@app.route('/contacts', methods=['GET'])
def retreive_contacts(addressbook):
    contacts = addressbook.get_contacts()

    return ok(contacts)


@inject(addressbook=services.AddressBook)
@app.route('/contacts/find', methods=['GET'])
def find_contacts(addressbook):
    phonenumber = request.args.get('phonenumber')
    contacts = addressbook.find_contact(phonenumber)

    return ok(contacts) if len(contacts) is not 0 else notfound()


@inject(addressbook=services.AddressBook)
@app.route('/contact/<contactid>', methods=['GET'])
def retreive_contact(contactid, addressbook):
    contact = addressbook.get_contact(contactid)

    return ok(contact)


@inject(addressbook=services.AddressBook)
@app.route('/contacts', methods=['POST'])
def create_contact(addressbook):
    contactinfo = request.get_json()
    addressbook.add_contact(contactinfo)

    return created()


@inject(addressbook=services.AddressBook)
@app.route('/contact/<contactid>', methods=['PUT'])
def update_contact(contactid, addressbook):
    contactinfo = request.get_json()
    addressbook.update_contact(contactid, contactinfo)

    return nocontent()


@inject(addressbook=services.AddressBook)
@app.route('/contact/<contactid>', methods=['DELETE'])
def delete_contact(contactid, addressbook):
    addressbook.remove_contact(contactid)

    return nocontent()

