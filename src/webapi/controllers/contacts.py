import repositories

from flask import request
from injector import inject
from webapi import app
from webapi.helpers.responses import *


@inject(contactrepo=repositories.ContactRepo)
@app.route('/contacts', methods=['GET'])
def retreive_contacts(contactrepo):
    contacts = contactrepo.get_contacts()

    return ok(contacts)


@inject(contactrepo=repositories.ContactRepo)
@app.route('/contacts/find', methods=['GET'])
def find_contacts(contactrepo):
    phonenumber = request.args.get('phonenumber')
    contacts = contactrepo.find_contact(phonenumber)

    return ok(contacts) if len(contacts) is not 0 else notfound()


@inject(contactrepo=repositories.ContactRepo)
@app.route('/contact/<contactid>', methods=['GET'])
def retreive_contact(contactid, contactrepo):
    contact = contactrepo.get_contact(contactid)

    return ok(contact)


@inject(contactrepo=repositories.ContactRepo)
@app.route('/contacts', methods=['POST'])
def create_contact(contactrepo):
    contactinfo = request.get_json()
    contactrepo.add_contact(contactinfo)

    return created()


@inject(contactrepo=repositories.ContactRepo)
@app.route('/contact/<contactid>', methods=['PUT'])
def update_contact(contactid, contactrepo):
    contactinfo = request.get_json()
    contactrepo.update_contact(contactid, contactinfo)

    return nocontent()


@inject(contactrepo=repositories.ContactRepo)
@app.route('/contact/<contactid>', methods=['DELETE'])
def delete_contact(contactid, contactrepo):
    contactrepo.remove_contact(contactid)

    return nocontent()

