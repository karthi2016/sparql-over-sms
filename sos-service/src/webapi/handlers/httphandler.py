from json import dumps
from tornado.web import RequestHandler
from datetime import datetime, timedelta
from tornado.ioloop import IOLoop
from persistence import message_repo
from utilities.messaging import to_response_category


class HttpHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def get_parameter(self, key, single=True, default=None):
        if type(key) is not str:
            raise TypeError('String expected')

        try:
            # prioritize query arguments over body arguments
            arguments = [arg.decode('UTF-8') for arg in self.request.arguments.get(key, self.request.body_arguments.get(key, None))]
            return arguments[0] if single else arguments
        except TypeError:
            return default

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
        self.write(dumps(dictionary))
        self.set_header("Content-Type", "application/json")
        self.finish()

    def write_listasjson(self, listing):
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
