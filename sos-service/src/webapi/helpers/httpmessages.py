from tornado.web import HTTPError


def badrequest(message):
    return HTTPError(400, message)


def timeout(message):
    return HTTPError(408, message)


def servererror(message):
    return HTTPError(500, message)
