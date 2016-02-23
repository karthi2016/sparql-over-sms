from flask import request
from webapi import app
from webapi.helpers.responses import *


@app.route('/incoming', methods=['POST'])
def incoming():
    body = request.get_json()
    print(body)

    return nocontent()
