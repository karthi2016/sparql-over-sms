from tornado.ioloop import IOLoop
from tornado.web import Application
from tornroutes import route
from webapi import endpoints


def make_app():
    return Application(route.get_routes())


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()
