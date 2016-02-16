import json

from webapi import app
from flask import Response, request


@app.route('/contacts', methods=['GET'])
def retreive_contacts():
    contactstore = app.config['c_contacts']
    contactids = app.config['c_contacts'].sections()

    contacts = []
    for contactid in contactids:
        contactinfo = contactstore[contactid]
        contact = {'contactid': contactid,
                   'fullname': contactinfo['fullname'],
                   'phonenumber': contactinfo['phonenumber']}

        contacts.append(contact)

    return Response(json.dumps(contacts), mimetype='application/json')


@app.route('/contact/<contactid>', methods=['GET'])
def retreive_contact(contactid):
    contactstore = app.config['c_contacts']
    contactinfo = contactstore[contactid]

    contact = {'contactid': contactid,
               'fullname': contactinfo['fullname'],
               'phonenumber': contactinfo['phonenumber']}

    return Response(json.dumps(contact), mimetype='application/json')


@app.route('/contacts', methods=['POST'])
def create_contact():
    contactstore = app.config['c_contacts']
    contactinfo = request.get_json()

    # create new contact
    contactid = contactinfo['contactid']
    contactstore.add_section(contactid)
    contactstore.set(contactid, 'fullname', contactinfo['fullname'])
    contactstore.set(contactid, 'phonenumber', contactinfo['phonenumber'])

    # persist changes
    with open(app.config['f_contacts'], 'w') as file:
        contactstore.write(file)

    return Response(status=201)


@app.route('/contact/<contactid>', methods=['PUT'])
def update_contact(contactid):
    contactstore = app.config['c_contacts']
    contactinfo = request.get_json()

    # update existing contact
    contact = contactstore[contactid]
    contact['fullname'] = contactinfo['fullname']
    contact['phonenumber'] = contactinfo['phonenumber']

    # persist changes
    with open(app.config['f_contacts'], 'w') as file:
        contactstore.write(file)

    return Response(status=204)


@app.route('/contact/<contactid>', methods=['DELETE'])
def delete_contact(contactid):
    contactstore = app.config['c_contacts']

    # remove contact form store
    contactstore.remove_section(contactid)

    # persist changes
    with open(app.config['f_contacts'], 'w') as file:
        contactstore.write(file)

    return Response(status=204)

