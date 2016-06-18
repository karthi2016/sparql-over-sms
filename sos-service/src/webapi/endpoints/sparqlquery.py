from tornroutes import route
from transfer.models import OutgoingMessage
from webapi.handlers import HttpHandler
from webapi.helpers import badrequest


@route('/agent/([\w]+)/sparql')
class SparqlQuery(HttpHandler):
    def data_received(self, chunk):
        pass

    def get(self, agentid):
        query = self.get_parameter('query')
        if query is None:
            raise badrequest('parameter "query" not provided')

        message = OutgoingMessage(1, query, agentid)
        self.write('{0}'.format(message))
