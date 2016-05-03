from webapi import app
from webapi.helpers.responses import *


@app.route('/')
def get_status():
    status = {'service': 'SPARQL over SMS', 'version': app.releaseversion}
    return ok(status, 'application/json')

