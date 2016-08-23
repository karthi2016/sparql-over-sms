import time

from persistence.repositories import MessageRepo
from timeit import default_timer as timer


class AwaitResponse:
    """Waits until a response message comes in"""
    name = 'AwaitResponse'
    description = 'Waits until a response messages arrives'

    @staticmethod
    def execute(token):
        messagerepo = MessageRepo()

        # retreive required information
        messageid = token.message.correlationid
        category = token.message.category

        # poll until response comes in
        response = None
        started = timer()
        while response is None:
            response = messagerepo.get_message_byidandcategory(messageid, category)

            # stop if timeout is reached
            elapsed = timer() - started
            if elapsed > 30:
                raise TimeoutError('timeout reached after 30s of polling')

            # don't flood it
            time.sleep(1)

        token.message.body = response.body
