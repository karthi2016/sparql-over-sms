from requests_futures.sessions import FuturesSession
from persistence import agent_repo


class HttpTransfer:
    """Transfers messages with HTTP"""
    max_bodysize = 135

    @staticmethod
    def send_single(receiver, body):
        self = agent_repo.get_byname('~self')

        url = 'http://{0}:8888/incoming'.format(receiver.hostname)
        session = FuturesSession()
        response_future = session.post(url, json={'sender': self.phonenumber, 'body': body})

        # wait for the response to come in
        response_future.result()

    @staticmethod
    def send_multiple(receiver, bodies):
        for body in bodies:
            HttpTransfer.send_single(receiver, body)

    @staticmethod
    def is_supported(receiver):
        return receiver.hostname is not None