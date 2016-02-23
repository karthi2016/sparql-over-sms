import configparser
import glob
import os
import services

from flask.ext.injector import FlaskInjector, singleton
from webapi import app

# load configuration
configuration = glob.glob('configuration/*.conf')
for file in configuration:
    config = configparser.ConfigParser()
    config.read(file)

    # use filename as key
    filename = os.path.splitext(os.path.basename(file))[0]
    app.config['c_{0}'.format(filename)] = config
    app.config['f_{0}'.format(filename)] = file


# bind dependencies
def configure(binder):
    addressbook = services.AddressBook(app.config['c_contacts'], app.config['f_contacts'])
    binder.bind(services.AddressBook, to=addressbook, scope=singleton)

    configmanager = services.ConfigManager(app.config)
    binder.bind(services.ConfigManager, to=configmanager, scope=singleton)

    messenger = services.Messenger(app.config['c_messaging'])
    binder.bind(services.Messenger, to=messenger, scope=singleton)

    rdfcompressor = services.RdfCompressor(app.config['c_compression'])
    binder.bind(services.RdfCompressor, to=rdfcompressor, scope=singleton)

    sparqlcompressor = services.SparqlCompressor(app.config['c_compression'])
    binder.bind(services.SparqlCompressor, to=sparqlcompressor, scope=singleton)


# bootstrap application
FlaskInjector(app=app, modules=[configure])
app.run(host='127.0.0.1', debug=True)
