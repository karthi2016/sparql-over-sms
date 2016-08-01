from tornroutes import route
from transfer.models import IncomingMessage
from transfer.constants import MessageCategory
from webapi.handlers import HttpHandler
from webapi.helpers import badrequest


@route('/incoming')
class Incoming(HttpHandler):

    def post(self):
        sender = self.get_parameter('sender')
        content = self.get_parameter('content')

        if sender is None:
            raise badrequest('parameter "sender" not provided')

        if content is None:
            raise badrequest('parameter "content" not provided')

        message = IncomingMessage(3, content, sender)
        self.write('{0}'.format(message))
        self.set_status(202)

