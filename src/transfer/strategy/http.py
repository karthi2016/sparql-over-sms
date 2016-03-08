import requests


class HttpTransfer:
    """Transfers messages with HTTP"""
    max_bodysize = 140000

    @staticmethod
    def send_single(receiver, body):
        url = 'http://{0}:5000/incoming'.format(receiver['hostname'])
        response = requests.post(url, json={'sender': 'unkown', 'body': body})
        print(response)

    @staticmethod
    def send_multiple(messages):
        raise NotImplementedError('Sending multiple messages via http')

    @staticmethod
    def is_supported(receiver):
        return receiver['hostname'] is not None

