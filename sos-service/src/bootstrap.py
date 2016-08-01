from tornado.ioloop import IOLoop
from tornado.web import Application
from tornroutes import route
from webapi import endpoints


def make_app():
    return Application(route.get_routes())


if __name__ == "__main__":
    port = 8888

    app = make_app()
    app.listen(port)

    print('The SPARQL over SMS service is listening on port {0}'.format(port))
    IOLoop.current().start()
