import json
from flask import Response


def ok(content, mimetype=None):
    body = content if type(content) is str else json.dumps(content)
    resp = Response(body, status=200, mimetype='application/json' if mimetype is None else mimetype)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


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

