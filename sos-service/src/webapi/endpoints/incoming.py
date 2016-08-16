from tornroutes import route
from transfer.models import IncomingMessage
from transfer.constants import MessageCategory
from webapi.handlers import HttpHandler
from webapi.helpers import badrequest
from persistence import messaging_uow
from utilities.messaging import extract_all


@route('/incoming')
class Incoming(HttpHandler):

    def post(self):
        sender = self.get_parameter('sender')
        content = self.get_parameter('content')

        if sender is None:
            raise badrequest('parameter "sender" not provided')

        if content is None:
            raise badrequest('parameter "content" not provided')

        # persist so it can be processed in the background
        correlationid, category, position, body = extract_all(content)
        messaging_uow.store_incoming(sender, correlationid, category, position, body)

        self.accepted()

