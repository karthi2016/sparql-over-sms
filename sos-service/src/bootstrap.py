from tornado.ioloop import IOLoop
from tornado.web import Application
from tornroutes import route
from webapi import endpoints
from persistence import database
from persistence.models import modelset


def initialize_db():
    database.connect()
    for model in modelset:
        database.create_table(model, safe=True)

    database.close()
    return database


def initialize_app():
    return Application(route.get_routes())


if __name__ == "__main__":
    port = 8888

    db = initialize_db()

    app = initialize_app()
    app.listen(port)


    print('The SPARQL over SMS service is listening on port {0}'.format(port))
    IOLoop.current().start()
