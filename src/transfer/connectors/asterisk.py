from requests_futures.sessions import FuturesSession


class AsteriskConnector:
    """Connector used to interface with Asterisk"""
    session = None

    def __init__(self, configmanager):
        config = configmanager.get_configuration('asterisk')

        # relevant config sections
        general = config['general']
        credentials = config['credentials']

        # configure Asterisk connector
        self.username = credentials['username']
        self.secret = credentials['secret']
        self.url = 'http://{0}:{1}/rawman'.format(general['host'], general['port'])
        self.dongleid = general['dongleid']

    def startsession(self):
        self.session = FuturesSession()
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
        future = self.session.get(self.url, params=parameters)
        return future.result()




