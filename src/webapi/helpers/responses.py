import json
from flask import Response


def ok(content):
    body = content if type(content) is str else json.dumps(content)
    return Response(body, status=200, mimetype='application/json')


def created():
    return Response(status=201)


def accepted():
    return Response(status=202)


def nocontent():
    return Response(status=204)

