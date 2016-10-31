from time import time

from tornroutes import route
from webapi.handlers import HttpHandler
from processing.tasks import verify_connection


@route('/healthcheck')
class HealthCheck(HttpHandler):

    def get(self):
        self.write('Task queue roundtrip: {0}s'.format(verify_connection.delay(time()).get()))
        self.set_status(200)
        self.finish()
