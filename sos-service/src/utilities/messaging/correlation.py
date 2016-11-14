from uuid import uuid4


def gen_correlationid():
    return uuid4().hex[:3]
