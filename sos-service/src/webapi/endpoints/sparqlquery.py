from uuid import uuid4
from tornado.web import asynchronous
from persistence import messaging_uow, message_repo
from processing import process_outgoingmessage
from tornroutes import route
from transfer.constants import MessageCategory
from webapi.handlers import HttpHandler
from webapi.helpers import badrequest, timeout, servererror


@route('/agent/([\w]+)/sparql')
class SparqlQuery(HttpHandler):

    @asynchronous
    def get(self, receiveraddress):
        query = self.get_parameter('query')

        if query is None:
            raise badrequest('parameter "query" not provided')

        # persist so it can be processed in the background
        correlationid = uuid4().hex[:3]
        message = messaging_uow.store_outgoing(receiveraddress, correlationid, MessageCategory.SPARQL_QUERY, 0, query)

        try:
            outgoing = process_outgoingmessage.delay(message.id)

            def check():
                send = outgoing.ready()
                if send:
                    received = message_repo.get_bycorrelation(correlationid, MessageCategory.SPARQL_QUERY_RESPONSE)
                    if received:
                        return True

                return False

            self.asyncwait(check, 1, 30, self.return_response, correlationid)

        except TimeoutError:
            raise timeout('the "process_outgoingmessage" operation has timed out')
        except Exception:
            raise servererror('the "process_outgoingmessage" operation failed')

    def return_response(self, correlationid):
        self.write(correlationid)
        self.set_header("Content-Type", "application/json")
        self.finish()
