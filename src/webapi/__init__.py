from flask import Flask
app = Flask(__name__)

import webapi.controllers.crud
import webapi.controllers.transfer
import webapi.controllers.index
