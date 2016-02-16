from flask import Flask
app = Flask(__name__)

import webapi.controllers.contacts
import webapi.controllers.messaging
import webapi.controllers.system
