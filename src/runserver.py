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


# register dependencies
def configure(binder):
    addressbook = services.AddressBook(app.config['c_contacts'], app.config['f_contacts'])
    binder.bind(services.AddressBook, to=addressbook, scope=singleton)


# bootstrap application
FlaskInjector(app=app, modules=[configure])
app.run(debug=True)
