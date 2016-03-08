import repositories


class StoreMessage:
    """Stores a message"""
    name = 'StoreMessage'
    description = 'Stores a message'

    @staticmethod
    def execute(token):
        # create a seperate instance of the message repository
        from webapi import app
        messagerepo = repositories.MessageRepo(app.config['c_persistence']['repositories']['message'])

        message = token.message
        messageid = '{0}-{1}'.format(message.correlationid, message.category)
        messagerepo.add_message(messageid, message.category, message.sender, message.body)

