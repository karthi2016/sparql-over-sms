#!/usr/bin/python
from argparse import ArgumentParser
from celery import Celery 


def run_worker():
    jobqueue = Celery()
    jobqueue.worker_main([
        'worker',
        '--app=processing',
        '--loglevel=INFO',
    ])


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('command', choices=['START', 'STOP', 'RESTART'])
    parser.add_argument('--background',
                        action="store_true",
                        help='when provided, the server will run in the background')

    # get input arguments
    arguments = parser.parse_args()

    pidfile = '/var/run/sos-worker.pid'
    command = arguments.command.upper()
    if command != 'START':
        from os import kill
        from signal import SIGTERM
        from errno import EPERM

        # stop the server
        pid = int(open(pidfile).read())
        try:
            kill(pid, SIGTERM)
            print('The SPARQL over SMS worker has been stopped.')
        except OSError as e:
            if e.errno == EPERM:
                exit(1)

        if command == 'STOP':
            exit(0)

    if arguments.background:
        from daemonize import Daemonize

        daemon = Daemonize(app="sos-worker", pid=pidfile, action=run_worker)
        daemon.start()
    else:
        run_worker()
