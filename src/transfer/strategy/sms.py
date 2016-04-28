from services.servicebox import ServiceBox
from transfer.connectors import AsteriskConnector


class SmsTransfer:
    """Transfers messages with SMS"""
    max_bodysize = 135

    @staticmethod
    def send_single(phonenumber, body):
        asterisk = ServiceBox.get_instance(AsteriskConnector)

        asterisk.startsession()
        asterisk.send_sms(phonenumber, body)

    @staticmethod
    def send_multiple(receiver, bodies):
        for body in bodies:
            SmsTransfer.send_single(receiver, body)

    @staticmethod
    def is_supported(receiver):
        return receiver['phonenumber'] is not None


