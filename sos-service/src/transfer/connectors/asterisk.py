import requests


class AsteriskConnector:
    """Connector used to interface with Asterisk"""
    session = None
    url = 'http://localhost:8088/rawman'

    def __init__(self, username, password, dongleid):
        self.username = username
        self.secret = password
        self.dongleid = dongleid

    def startsession(self):
        self.session = requests.Session()
        self.authenticate()

    def authenticate(self):
        parameters = {'action': 'login', 'username': self.username, 'secret': self.secret}
        self.send_request(parameters)

    def send_sms(self, phonenumber, content):
        command = 'dongle sms {0} {1} {2}'.format(self.dongleid, phonenumber, content)
        return self.send_command(command)

    def send_command(self, command):
        parameters = {'action': 'command', 'command': command}
        return self.send_request(parameters)

    def send_request(self, parameters):
        return self.session.get(self.url, params=parameters)
