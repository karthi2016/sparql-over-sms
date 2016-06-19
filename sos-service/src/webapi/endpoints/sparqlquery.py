from processing.models import OutgoingPipelineToken
from processing.pipelines import SendSparqlQuery
from tornroutes import route
from transfer.models import OutgoingMessage
from webapi.handlers import HttpHandler
from webapi.helpers import badrequest, timeout, servererror


@route('/agent/([\w]+)/sparql')
class SparqlQuery(HttpHandler):

    def get(self, agentid):
        query = self.get_parameter('query')

        if query is None:
            raise badrequest('parameter "query" not provided')

        message = OutgoingMessage(1, query, agentid)
        token = OutgoingPipelineToken(message)

        try:
            result = SendSparqlQuery.execute(token)
        except TimeoutError:
            raise timeout('the "SendSparqlQuery" operation has timed out')
        except Exception:
            raise servererror('the "SendSparqlQuery" operation failed')

        self.write(result)
        self.set_status(200)
