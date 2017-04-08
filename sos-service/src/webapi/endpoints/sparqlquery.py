from tornado.web import asynchronous
from persistence import messaging_uow
from processing import process_outgoingmessage
from tornroutes import route
from transfer.constants import MessageCategory
from utilities.messaging.correlation import gen_correlationid
from webapi.handlers import HttpHandler
from webapi.helpers import badrequest, timeout, servererror


@route('/agent/([+|~]?\w+)/sparql')
class SparqlQuery(HttpHandler):

    @asynchronous
    def get(self, receiveraddress):
        query = self.get_parameter('query')

        if query is None:
            raise badrequest('parameter "query" not provided')

        # persist so it can be processed in the background
        correlationid = gen_correlationid()
        message = messaging_uow.store_outgoing(receiveraddress, correlationid, MessageCategory.SPARQL_QUERY, query)

        try:
            outgoing = process_outgoingmessage.delay(message.id)

            def check(): return outgoing.ready() and messaging_uow.is_answered(message)
            self.asyncwait(check, 1, 30, self.write_responsetomessage, message)

        except TimeoutError:
            raise timeout('the incoming "SparqlQuery" request has timed out')
        except Exception:
            raise servererror('the incoming "SparqlQuery" request failed')
