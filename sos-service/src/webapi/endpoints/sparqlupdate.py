from tornado.web import asynchronous
from persistence import messaging_uow
from processing import process_outgoingmessage
from tornroutes import route
from transfer.constants import MessageCategory
from utilities.messaging.correlation import gen_correlationid
from webapi.handlers import HttpHandler
from webapi.helpers import badrequest, timeout, servererror


@route('/agent/([+|~]?\w+)/sparql/update')
class SparqlUpdate(HttpHandler):

    @asynchronous
    def post(self, receiveraddress):
        update = self.get_parameter('update')

        if update is None:
            raise badrequest('parameter "update" not provided')

        # persist so it can be processed in the background
        correlationid = gen_correlationid()
        message = messaging_uow.store_outgoing(receiveraddress, correlationid, MessageCategory.SPARQL_UPDATE, update)

        try:
            outgoing = process_outgoingmessage.delay(message.id)

            def check(): return outgoing.ready() and messaging_uow.is_answered(message)
            self.asyncwait(check, 1, 30, self.write_responsetomessage, message)

        except TimeoutError:
            raise timeout('the incoming "SparqlUpdate" request has timed out')
        except Exception:
            raise servererror('the incoming "SparqlUpdate" request failed')
