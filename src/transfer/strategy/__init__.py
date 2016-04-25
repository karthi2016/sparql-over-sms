from transfer.strategy.http import HttpTransfer
from transfer.strategy.sms import SmsTransfer

# prioritized list (descending costs)
transfer_strategies = [
    HttpTransfer,
    SmsTransfer
]
