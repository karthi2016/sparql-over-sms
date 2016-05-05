import json
import datetime
from flask import Response


def default(o):
    if type(o) is datetime.date or type(o) is datetime.datetime:
        return o.isoformat()

def ok(content, mimetype):
    body = content if type(content) is str else json.dumps(content, default=default)
    return Response(body, status=200, mimetype=mimetype)

def created():
    return Response(status=201)


def accepted():
    return Response(status=202)


def nocontent():
    return Response(status=204)


def badrequest():
    return Response(status=400)


def notfound():
    return Response(status=404)


def timeout():
    return Response(status=408)


def servererror():
    return Response(status=500)


def notimplemented():
    return Response(status=501)

