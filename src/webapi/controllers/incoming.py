from webapi import app
from webapi.helpers.responses import *


@app.route('/incoming', methods=['POST'])
def incoming():
    return notimplemented()
