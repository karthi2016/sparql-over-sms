from webapi.handlers import HttpHandler
from tornroutes import route


@route('/agent/([\w]+)/sparql/update')
class SparqlUpdate(HttpHandler):
    def data_received(self, chunk):
        pass

    def get(self, agentid):
        self.write(agentid)
