#!/usr/bin/python
from argparse import ArgumentParser
from celery import Celery
from utilities import configmanager


default_taskqueue = 'localhost'
default_triplestore = 'localhost'


def run():
    jobqueue = Celery()
    jobqueue.worker_main([
        'worker',
        '--app=processing',
        '--loglevel=INFO',
    ])


def run_worker():
    parser = ArgumentParser()
    parser.add_argument('command', choices=['START', 'STOP', 'RESTART'])

    parser.add_argument('--taskqueue',  type=str, default=default_taskqueue,
                        help='hostname of the taskqueue (default: {0})'.format(default_taskqueue))

    parser.add_argument('--triplestore', type=str, default=default_triplestore,
                        help='hostname of the triplestore (default: {0})'.format(default_triplestore))

    parser.add_argument('--background', action="store_true",
                        help='when provided, the server will run in the background')

    arguments = parser.parse_args()

    pidfile = '/var/run/sos-worker.pid'
    command = arguments.command.upper()
    if command != 'START':
        from os import kill
        from signal import SIGTERM
        from errno import EPERM

        # stop the worker
        pid = int(open(pidfile).read())
        try:
            kill(pid, SIGTERM)
            print('The SPARQL over SMS worker has been stopped.')
        except OSError as e:
            if e.errno == EPERM:
                exit(1)

        if command == 'STOP':
            exit(0)

    # configure worker
    configmanager.set_config('taskqueue_host', arguments.taskqueue)
    configmanager.set_config('triplestore_host', arguments.triplestore)

    if arguments.background:
        from daemonize import Daemonize

        daemon = Daemonize(app="sos-worker", pid=pidfile, action=run)
        daemon.start()
    else:
        run()


if __name__ == "__main__":
    run_worker()
