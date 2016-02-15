from flask import request
from webapi import app
from connectors import AsteriskConnector


@app.route('/outgoing-message', methods=['POST'])
def send_message():
    receiver = request.form.get('receiver')
    message = request.form.get('message')

    print('{0} - {1}'.format(receiver, message))
    asterisk = AsteriskConnector(app.config['c_asterisk'], app.config['c_contacts'])
    response = asterisk.send_sms(receiver, message)
    return response.content


@app.route('/incoming-message', methods=['POST'])
def receive_message():
    unqueid = request.form.get('uniqueid')
    sender = request.form.get('sender')
    message = request.form.get('message')

    print('Incoming: {0} ({1}, {2})'.format(message, unqueid, sender))





