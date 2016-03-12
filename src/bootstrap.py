import configparser
import glob
import os
import repositories
import services
import transfer

from repositories import ContactRepo, MessageRepo
from flask_injector import FlaskInjector
from injector import singleton
from services import ConfigManager, ServiceBox
from webapi import app
from transfer import Messenger

# load configuration
configuration = glob.glob('configuration/*.conf')
for file in configuration:
    config = configparser.ConfigParser()
    config.read(file)

    # use filename as key
    filename = os.path.splitext(os.path.basename(file))[0]
    app.config['c_{0}'.format(filename)] = config
    app.config['f_{0}'.format(filename)] = file


# populate ioc container
contactrepo = repositories.ContactRepo(app.config['c_contacts'], app.config['f_contacts'])
ServiceBox.register_instance(ContactRepo, contactrepo)

messagerepo = repositories.MessageRepo(app.config['c_persistence']['repositories']['message'])
ServiceBox.register_instance(MessageRepo, messagerepo)

configmanager = services.ConfigManager(app.config)
ServiceBox.register_instance(ConfigManager, configmanager)

messenger = Messenger(contactrepo)
ServiceBox.register_instance(Messenger, messenger)


# bind dependencies
def configure(binder):
    binder.bind(repositories.ContactRepo, to=contactrepo, scope=singleton)
    binder.bind(repositories.MessageRepo, to=messagerepo, scope=singleton)
    binder.bind(services.ConfigManager, to=configmanager, scope=singleton)
    binder.bind(transfer.Messenger, to=messenger, scope=singleton)

# bootstrap application
app.injector = FlaskInjector(app=app, modules=[configure])
if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
