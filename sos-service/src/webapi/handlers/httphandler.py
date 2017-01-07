from json import dumps, loads
from tornado.web import RequestHandler
from datetime import datetime, timedelta
from tornado.ioloop import IOLoop
from persistence import message_repo
from utilities.messaging import to_response_category


class HttpHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
        self.set_header('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE, OPTIONS')

    def get_parameter(self, key, default=None):
        if type(key) is not str:
            raise TypeError('String expected')

        request = self.request
        if 'application/json' in request.headers.get('Content-Type', ''):
            body_arguments = loads(request.body.decode('UTF-8'))
        else:
            body_arguments = request.body_arguments

        parameter = request.arguments.get(key, body_arguments.get(key, None))
        parameter = parameter[0] if type(parameter) is list else parameter
        parameter = parameter.decode('UTF-8') if type(parameter) is bytes else parameter

        return parameter if parameter is not None else default

    def asyncwait(self, check, s_interval, s_timeout, callback, args):
        if type(s_timeout) is int:
            s_timeout = datetime.now() + timedelta(seconds=s_timeout)

        # check if timeout is reached
        if s_timeout < datetime.now():
            raise TimeoutError("The 'asyncwait' operation timed-out.")

        satisfy = check()
        if satisfy:
            callback(args)
        else:
            IOLoop.instance().add_timeout(timedelta(seconds=s_interval), self.asyncwait, check, s_interval, s_timeout, callback, args)

    def write_responsetomessage(self, message):
        correlationid = message.correlationid
        responsecategory = to_response_category(message.category)

        response = message_repo.get_bycorrelation(correlationid, responsecategory)

        self.write(response.get_body())
        self.set_header("Content-Type", "text/turtle")
        self.finish()

    def write_dictasjson(self, dictionary):
        self.set_status(200)
        self.write(dumps(dictionary))
        self.set_header('Content-Type', 'application/json')
        self.finish()

    def write_listasjson(self, listing):
        self.set_status(200)
        self.write(dumps(listing))
        self.set_header("Content-Type", "application/json")
        self.finish()

    def accepted(self):
        self.set_status(202)
        self.finish()

    def notfound(self):
        self.set_status(404)
        self.finish()

    def internalerror(self):
        self.set_status(500)
        self.finish()
