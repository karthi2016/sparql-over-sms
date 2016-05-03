import json
from flask import Response


def ok(content, mimetype):
    body = content if type(content) is str else json.dumps(content)
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

