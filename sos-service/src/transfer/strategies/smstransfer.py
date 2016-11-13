from transfer.connectors import AsteriskConnector


class SmsTransfer:
    """Transfers messages with SMS"""
    max_bodysize = 135

    @staticmethod
    def send_single(receiver, body):
        asterisk = AsteriskConnector('spam', 'eggs', 'dongle0')

        asterisk.startsession()
        asterisk.send_sms(receiver.phonenumber, body)

    @staticmethod
    def send_multiple(receiver, bodies):
        for body in bodies:
            SmsTransfer.send_single(receiver, body)

    @staticmethod
    def is_supported(receiver):
        return receiver.phonenumber is not None
