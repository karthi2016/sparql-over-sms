from webapi import app
from webapi.helpers.responses import *


@app.route('/')
def get_status():
    return ok({'name': 'Semantic M2M', 'version': '0.0.0'})





