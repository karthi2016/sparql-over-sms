from tornado.web import RequestHandler


class HttpHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def get_parameter(self, key, single=True):
        if type(key) is not str:
            raise TypeError('String expected')

        try:
            arguments = [arg.decode('utf-8') for arg in self.request.arguments[key]]
            return arguments[0] if single else arguments
        except KeyError:
            return None

    def accepted(self):
        self.set_status(202)
