from transfer.strategy.http import HttpTransfer
from transfer.strategy.sms import SmsTransfer

# prioritized list
transfer_strategies = [
    HttpTransfer,
    SmsTransfer
]
