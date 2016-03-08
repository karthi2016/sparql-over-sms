from flask import Flask
app = Flask(__name__)

# load controllers into scope
import webapi.controllers.configuration
import webapi.controllers.contacts
import webapi.controllers.incoming
import webapi.controllers.system
import webapi.controllers.query
