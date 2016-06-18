from tornado.web import HTTPError


def badrequest(message):
    return HTTPError(400, message)
