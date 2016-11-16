from argparse import ArgumentParser
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornroutes import route
from webapi import endpoints
from persistence import database
from persistence.models import model_list


default_port = 8888
default_database = 'sparqloversms.db'


def initialize_db():
    database.connect()
    for model in model_list:
        database.create_table(model, safe=True)

    database.close()
    return database


def initialize_app():
    return Application(route.get_routes())


def run_server(port, database):
    db = initialize_db()
    app = initialize_app()

    # configure application
    app.listen(port)

    # start main IO loop
    print('The SPARQL over SMS service is listening on port {0}.'.format(port))
    IOLoop.current().start()

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('command', choices=['START', 'STOP', 'RESTART'])
    parser.add_argument('--port',
                        type=int,
                        nargs=1,
                        default=default_port,
                        help='the port the server will use (default: {0})'.format(default_port))
    parser.add_argument('--database',
                        type=str,
                        nargs=1,
                        default=default_database,
                        help='filepath to database file (default: {0})'.format(default_database))
    parser.add_argument('--background',
                        action="store_true",
                        help='when provided, the server will run in the background')

    # get input arguments
    arguments = parser.parse_args()

    def run():
        run_server(arguments.port, arguments.background)

    pidfile = '/var/run/sos-server.pid'
    command = arguments.command.upper()
    if command != 'START':
        from os import kill
        from signal import SIGTERM
        from errno import EPERM

        # stop the server
        pid = int(open(pidfile).read())
        try:
            kill(pid, SIGTERM)
            print('The SPARQL over SMS server has been stopped.')
        except OSError as e:
            if e.errno == EPERM:
                exit(1)

        if command == 'STOP':
            exit(0)

    if arguments.background:
        from daemonize import Daemonize

        daemon = Daemonize(app="sos-server", pid=pidfile, action=run)
        daemon.start()
    else:
        run()
