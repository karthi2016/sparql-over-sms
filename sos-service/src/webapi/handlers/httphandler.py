from tornado.web import RequestHandler


class HttpHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def get_parameter(self, key, single=True):
        if type(key) is not str:
            raise TypeError('String expected')

        # prioritize query arguments over body arguments
        arguments = [arg.decode('UTF-8') for arg in self.request.arguments.get(key, self.request.body_arguments.get(key, None))]
        return arguments[0] if single else arguments

    def accepted(self):
        self.set_status(202)

