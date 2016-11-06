from uuid import uuid4
from tornado import gen
from persistence import messaging_uow
from processing import process_outgoingmessage
from tornroutes import route
from transfer.constants import MessageCategory
from webapi.handlers import HttpHandler
from webapi.helpers import badrequest, timeout, servererror


@route('/agent/([\w]+)/sparql/update')
class SparqlUpdate(HttpHandler):

    @gen.coroutine
    def post(self, receiveraddress):
        update = self.get_parameter('update')

        if update is None:
            raise badrequest('parameter "update" not provided')

        # persist so it can be processed in the background
        correlationid = uuid4().hex[:3]
        message = messaging_uow.store_outgoing(receiveraddress, correlationid, MessageCategory.SPARQL_UPDATE, 0, update)

        try:
            result = process_outgoingmessage.delay(message.id).get()
        except TimeoutError:
            raise timeout('the "process_outgoingmessage" operation has timed out')
        except Exception:
            raise servererror('the "process_outgoingmessage" operation failed')

        self.write(result)
        self.set_status(200)
