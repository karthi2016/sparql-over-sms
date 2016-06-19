from tornroutes import route
from transfer.models import OutgoingMessage
from webapi.handlers import HttpHandler
from webapi.helpers import badrequest


@route('/agent/([\w]+)/sparql/update')
class SparqlUpdate(HttpHandler):

    def post(self, agentid):
        update = self.get_parameter('update')

        if update is None:
            raise badrequest('parameter "update" not provided')

        message = OutgoingMessage(2, update, agentid)
        self.write('{0}'.format(message))
        self.set_status(200)
