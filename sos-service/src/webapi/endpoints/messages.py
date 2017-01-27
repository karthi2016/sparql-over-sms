from tornroutes import route

from utilities.conversion import convertrdf_bymimetype
from webapi.handlers import HttpHandler
from persistence import message_repo


@route('/messages')
class MessagesEndpoint(HttpHandler):

    def get(self):
        page = self.get_parameter('page', default=1)
        items = self.get_parameter('items', default=25)

        messages = message_repo.get_all_outgoing(int(page), int(items))
        messages_list = [message.as_dict() for message in messages]

        self.write_listasjson(messages_list)

    def options(self):
        self.set_status(204)
        self.finish()


@route('/message/(\w+)')
class MessageEndpoint(HttpHandler):

    def delete(self, correlationid):
        outgoing_message = message_repo.get_outgoing_bycorrelation(correlationid)
        incoming_message = message_repo.get_incoming_bycorrelation(correlationid)

        if outgoing_message is not None:
            message_repo.delete(outgoing_message)

        if incoming_message is not None:
            message_repo.delete(incoming_message)

    def options(self, correlationid):
        self.set_status(204)
        self.finish()


@route('/message/(\w+)/request')
class RequestMessageEndpoint(HttpHandler):

    def get(self, correlationid):
        message = message_repo.get_outgoing_bycorrelation(correlationid)
        if message is None:
            self.notfound()
            return

        self.write_dictasjson(message.as_dict())


@route('/message/(\w+)/response')
class ResponseMessageEndpoint(HttpHandler):

    def get(self, correlationid):
        message = message_repo.get_incoming_bycorrelation(correlationid)
        if message is None:
            self.notfound()
            return

        message_dict = message.as_dict()
        try:
            message_dict['body'] = convertrdf_bymimetype(message_dict['body'], 'text/turtle').decode('utf-8')
        except:
            pass

        self.write_dictasjson(message_dict)

    def options(self, correlationid):
        self.set_status(204)
        self.finish()

