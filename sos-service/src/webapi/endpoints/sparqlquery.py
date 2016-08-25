from processing.models import OutgoingPipelineToken
from processing.pipelines import SendSparqlQuery
from tornroutes import route
from transfer.models import OutgoingMessage
from transfer.constants import MessageCategory
from webapi.handlers import HttpHandler
from webapi.helpers import badrequest, timeout, servererror
from tornado import web


@route('/agent/([\w]+)/sparql')
class SparqlQuery(HttpHandler):

    #@web.asynchronous
    def get(self, agentid):
        query = self.get_parameter('query')

        if query is None:
            raise badrequest('parameter "query" not provided')

        message = OutgoingMessage(MessageCategory.SPARQL_QUERY, query, agentid)
        token = OutgoingPipelineToken(message)

        try:
            result = SendSparqlQuery.execute(token)
        except TimeoutError:
            raise timeout('the "SendSparqlQuery" operation has timed out')
        except Exception:
            raise servererror('the "SendSparqlQuery" operation failed')

        self.write(result)
        self.set_status(200)

        # process_incomingmessage.apply_async(args=[message.id], callback=self.on_result)

        # def on_result(self, response):
        #    self.write(str(response.result))
        #    self.finish()

