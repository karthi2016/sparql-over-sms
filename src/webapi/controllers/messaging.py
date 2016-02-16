from base64 import b64decode
from flask import request
from webapi import app
from connectors import AsteriskConnector, SPARQLConnector


@app.route('/outgoing-message', methods=['POST'])
def outgoing_message():
    receiver = request.form.get('receiver')
    message = request.form.get('message')

    asterisk = AsteriskConnector(app.config['c_asterisk'], app.config['c_contacts'])
    response = asterisk.send_sms(receiver, message)
    return response.content


@app.route('/incoming-message', methods=['POST'])
def incoming_message():
    sender = request.form.get('sender')
    message = b64decode(request.form.get('message').replace(' ', '+')).decode("utf-8")

    sub, pred, obj = message.split(' ', 2)
    print('{0}: {1}'.format(sender, '{0} {1} {2}'.format(sub, pred, obj)))

    sparql = SPARQLConnector(app.config['c_triplestore'])
    sparql.insert(sub, pred, obj)

    # TODO: proper response object with status code, etc.
    return 'accepted'





