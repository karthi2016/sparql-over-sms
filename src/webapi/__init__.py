from flask import Flask
app = Flask(__name__)

import webapi.controllers.index

# load system controllers
import webapi.controllers.system.configuration
import webapi.controllers.system.contacts
import webapi.controllers.system.messages

# load transfer controllers
import webapi.controllers.transfer.graphstore
import webapi.controllers.transfer.incoming
import webapi.controllers.transfer.sparql
