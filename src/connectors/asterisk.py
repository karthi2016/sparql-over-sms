import requests


class AsteriskConnector:
    """Connector used for communication with Asterisk"""

    def __init__(self, config, contacts):
        self.config = config
        self.contacts = contacts
        self.session = requests.Session()

        general = config['general']
        self.host = general['host']
        self.port = general['port']
        self.dongleid = general['dongleid']

        credentials = config['credentials']
        self.authenticate(credentials['username'], credentials['secret'])

    def authenticate(self, username, secret):
        parameters = {'action': 'login', 'username': username, 'secret': secret}
        self.send_request(parameters)

    def send_sms(self, contactid, content):
        contactnr = self.contacts[contactid]['phonenumber']
        command = 'dongle sms dongle0 {0} {1}'.format(self.dongleid, contactnr, content)
        return self.send_command(command)

    def send_command(self, command):
        parameters = {'action': 'command', 'command': command}
        return self.send_request(parameters)

    def send_request(self, parameters):
        url = 'http://{0}:{1}/rawman'.format(self.host, self.port)
        return self.session.get(url, params=parameters)




