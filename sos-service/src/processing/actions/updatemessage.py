from persistence import message_repo


class UpdateMessage:
    """Updates a message"""
    name = 'UpdateMessage'
    description = 'Updates a message'

    @staticmethod
    def execute(token):
        message = token.message
        message_repo.update(message)
