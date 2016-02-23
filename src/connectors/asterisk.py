import requests


class AsteriskConnector:
    """Connector used for communication with Asterisk"""

    def __init__(self, asteriskconfig):
        self.session = requests.Session()

        general = asteriskconfig['general']
        self.host = general['host']
        self.port = general['port']
        self.dongleid = general['dongleid']

        credentials = asteriskconfig['credentials']
        self.authenticate(credentials['username'], credentials['secret'])

    def authenticate(self, username, secret):
        parameters = {'action': 'login', 'username': username, 'secret': secret}
        self.send_request(parameters)

    def send_sms(self, phonenumber, content):
        command = 'dongle sms dongle0 {0} {1}'.format(phonenumber, content)
        return self.send_command(command)

    def send_command(self, command):
        parameters = {'action': 'command', 'command': command}
        return self.send_request(parameters)

    def send_request(self, parameters):
        url = 'http://{0}:{1}/rawman'.format(self.host, self.port)
        return self.session.get(url, params=parameters)




