from processing.models import OutgoingPipelineToken
from processing.pipelines import SendSparqlUpdate
from tornroutes import route
from transfer.models import OutgoingMessage
from transfer.constants import MessageCategory
from webapi.handlers import HttpHandler
from webapi.helpers import badrequest, timeout, servererror


@route('/agent/([\w]+)/sparql/update')
class SparqlUpdate(HttpHandler):

    def post(self, agentid):
        update = self.get_parameter('update')

        if update is None:
            raise badrequest('parameter "update" not provided')

        message = OutgoingMessage(MessageCategory.SPARQL_UPDATE, update, agentid)
        token = OutgoingPipelineToken(message)

        try:
            result = SendSparqlUpdate.execute(token)
        except TimeoutError:
            raise timeout('the "SendSparqlUpdate" operation has timed out')
        except Exception:
            raise servererror('the "SendSparqlUpdate" operation failed')

        self.write(result)
        self.set_status(200)
