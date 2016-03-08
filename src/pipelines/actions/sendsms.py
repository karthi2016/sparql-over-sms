from repositories import ContactRepo
from transfer import Messenger


class SendSms:
    """Sends a sms"""
    name = "SendSms"
    description = "Send a sms"

    @staticmethod
    def execute(token):
        from webapi import app

        contactrepo = ContactRepo(app.config['c_contacts'], app.config['f_contacts'])

        messenger = Messenger(contactrepo)
        messenger.send(token.message)









