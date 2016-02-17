import json

from flask import Response
from webapi import app


@app.route('/')
def get_status():
    status = {
        'name': 'Semantic M2M',
        'version': '0.0.0',
    }

    return Response(json.dumps(status), mimetype='application/json')




