from persistence.repositories import ContactRepo
from requests_futures.sessions import FuturesSession
from services import ServiceBox


class HttpTransfer:
    """Transfers messages with HTTP"""
    max_bodysize = 135

    @staticmethod
    def send_single(receiver, body):
        contactrepo = ServiceBox.get_instance(ContactRepo)
        self = contactrepo.get_contact_byid('self')

        url = 'http://{0}:5000/incoming'.format(receiver.ip)
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
        return receiver.ip is not None

