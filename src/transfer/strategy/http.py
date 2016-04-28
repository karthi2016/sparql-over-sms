import requests


class HttpTransfer:
    """Transfers messages with HTTP"""
    max_bodysize = 135

    @staticmethod
    def send_single(receiver, body):
        url = 'http://{0}:5000/incoming'.format(receiver['hostname'])
        response = requests.post(url, json={'sender': '+31626056615', 'body': body})

    @staticmethod
    def send_multiple(receiver, bodies):
        for body in bodies:
            HttpTransfer.send_single(receiver, body)

    @staticmethod
    def is_supported(receiver):
        return receiver['hostname'] is not None

