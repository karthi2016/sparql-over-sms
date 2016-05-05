import configparser
import os
import glob
import services
import transfer

from flask_injector import FlaskInjector
from flask.ext.cors import CORS
from injector import singleton
from services import ConfigManager, ServiceBox
from webapi import app
from transfer import Messenger
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from os import path
from argparse import ArgumentParser

# parse arguments
parser = ArgumentParser(description='SPARQL over SMS')
parser.add_argument('--processes', default=1, type=int, help='number of processes (default: 1)')
parser.add_argument('--port', default=5000, type=int, help='port number to bind (default: 5000)')
args = parser.parse_args()

# load configuration
sources = path.dirname(path.abspath(__file__))
configuration = glob.glob(path.join(sources, 'configuration/*.conf'))
for file in configuration:
    config = configparser.ConfigParser()
    config.read(file)

    # use filename as key
    filename = path.splitext(path.basename(file))[0]
    app.config['c_{0}'.format(filename)] = config
    app.config['f_{0}'.format(filename)] = file

# populate ioc container
configmanager = services.ConfigManager(app.config)
ServiceBox.register_instance(ConfigManager, configmanager)

messenger = Messenger('asdf')
ServiceBox.register_instance(Messenger, messenger)

# bind dependencies
def configure(binder):
    binder.bind(services.ConfigManager, to=configmanager, scope=singleton)
    binder.bind(transfer.Messenger, to=messenger, scope=singleton)

# bootstrap application
with open(path.join(path.dirname(sources), 'releaseversion.txt'), 'r') as f:
    app.releaseversion = f.readline()

app.injector = FlaskInjector(app=app, modules=[configure])
CORS(app)
if __name__ == "__main__":
    http_server = HTTPServer(WSGIContainer(app))
    http_server.bind(args.port)
    http_server.start(args.processes)
    print('SPARQL over SMS started (port: {0}, pid: {1})'.format(args.port, os.getpid()))
    IOLoop.current().start()
