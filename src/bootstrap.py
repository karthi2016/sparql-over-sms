import configparser
import glob
import os
import repositories
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
    contactrepo = repositories.ContactRepo(app.config['c_contacts'], app.config['f_contacts'])
    binder.bind(repositories.ContactRepo, to=contactrepo, scope=singleton)

    configmanager = services.ConfigManager(app.config)
    binder.bind(services.ConfigManager, to=configmanager, scope=singleton)


# bootstrap application
FlaskInjector(app=app, modules=[configure])
if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)