from uuid import uuid4

import datetime
from tornado.ioloop import IOLoop
from tornado.web import asynchronous
from persistence import messaging_uow
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
            task = process_outgoingmessage.delay(message.id)

            def check_celery_task():
                if task.ready():
                    self.write(task.get().message.get_body())
                    self.set_header("Content-Type", "application/json")
                    self.finish()
                else:
                    IOLoop.instance().add_timeout(datetime.timedelta(0.00001), check_celery_task)

            IOLoop.instance().add_timeout(datetime.timedelta(0.00001), check_celery_task)

        except TimeoutError:
            raise timeout('the "process_outgoingmessage" operation has timed out')
        except Exception:
            raise servererror('the "process_outgoingmessage" operation failed')
