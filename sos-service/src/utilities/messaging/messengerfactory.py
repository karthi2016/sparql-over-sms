from transfer.strategies.httptransfer import HttpTransfer
from utilities.messaging.messenger import Messenger


class MessengerFactory:
    
    @staticmethod
    def get_messenger(receiver):
        return Messenger(HttpTransfer)
