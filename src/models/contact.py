from models import Model


class Contact(Model):
    """Contact representation"""

    def __init__(self, identifier, name, phonenumber, ip=None):
        self.identifier = identifier
        self.name = name
        self.phonenumber = phonenumber
        self.ip = ip
