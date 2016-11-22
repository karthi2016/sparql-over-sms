from argparse import ArgumentParser
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornroutes import route
from utilities import configmanager
from persistence import database, agent_repo
from persistence.models import model_list


default_port = 8888
default_taskqueue = 'localhost'
default_triplestore = 'localhost'


def initialize_db():
    database.connect()
    for model in model_list:
        database.create_table(model, safe=True)

    _self = agent_repo.get_byname("~self", create_if_nonexist=True)
    _self.hostname = 'localhost'
    _self.save()

    database.close()
    return database


def initialize_app(port):
    app = Application(route.get_routes())
    app.listen(port)
    return app


def run(port, taskqueue_host, triplestore_host):
    configmanager.set_config('taskqueue_host', taskqueue_host)
    configmanager.set_config('triplestore_host', triplestore_host)

    from webapi import endpoints

    db = initialize_db()
    app = initialize_app(port)

    # start main IO loop
    print('The SPARQL over SMS service is listening on port {0}.'.format(port))
    IOLoop.current().start()


def run_server():
    parser = ArgumentParser()
    parser.add_argument('command', choices=['START', 'STOP', 'RESTART'])

    parser.add_argument('--port', type=int, default=default_port,
                        help='the port the server will use (default: {0})'.format(default_port))

    parser.add_argument('--taskqueue', type=str, default=default_taskqueue,
                        help='hostname of the taskqueue (default: {0})'.format(default_taskqueue))

    parser.add_argument('--triplestore', type=str, default=default_triplestore,
                        help='hostname of the triplestore (default: {0})'.format(default_triplestore))

    parser.add_argument('--background', action="store_true",
                        help='when provided, the server will run in the background')

    arguments = parser.parse_args()

    def args_run():
        run(arguments.port, arguments.taskqueue, arguments.triplestore)

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

        daemon = Daemonize(app="sos-server", pid=pidfile, action=args_run)
        daemon.start()
    else:
        args_run()

if __name__ == "__main__":
    run_server()