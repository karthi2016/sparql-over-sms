from tornroutes import route
from webapi.handlers import HttpHandler
from persistence import message_repo


@route('/messages')
class MessagesEndpoint(HttpHandler):

    def get(self):
        page = self.get_parameter('page', default=1)
        items = self.get_parameter('items', default=25)

        messages = message_repo.get_all(int(page), int(items))
        messages_list = [message.as_dict() for message in messages]

        self.write_listasjson(messages_list)

    def options(self):
        self.set_status(204)
        self.finish()


@route('/message/([0-9]+)')
class MessageEndpoint(HttpHandler):

    def get(self, messageid):
        message = message_repo.get_byid(messageid)
        if message is None:
            self.notfound()
            return

        self.write_dictasjson(message.as_dict())

    def delete(self, messageid):
        message = message_repo.get_byid(messageid)
        if message is None:
            self.notfound()
            return

        # delete message
        agent = message_repo.delete(message)
        if agent is None:
            self.internalerror()
            return

        self.write_dictasjson(message.as_dict())

    def options(self, messageid):
        self.set_status(204)
        self.finish()
