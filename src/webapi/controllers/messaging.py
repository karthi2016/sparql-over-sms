import json

from base64 import b64decode
from flask import Response, request
from webapi import app
from connectors import AsteriskConnector, TripleStoreConnector


@app.route('/outgoing-message', methods=['POST'])
def outgoing_message():
    receiver = request.form.get('receiver')
    message = request.form.get('message')

    asterisk = AsteriskConnector(app.config['c_asterisk'], app.config['c_contacts'])
    outcome = asterisk.send_sms(receiver, message).content.decode('utf-8')

    response = {'outcome': outcome}
    return Response(json.dumps(response), mimetype='application/json')


@app.route('/incoming-message', methods=['POST'])
def incoming_message():
    sender = request.form.get('sender')
    message = b64decode(request.form.get('message').replace(' ', '+')).decode('utf-8')

    sub, pred, obj = message.split(' ', 2)
    print('{0}: {1}'.format(sender, '{0} {1} {2}'.format(sub, pred, obj)))

    sparql = TripleStoreConnector(app.config['c_triplestore'])
    sparql.insert(sub, pred, obj)

    return Response(202)





