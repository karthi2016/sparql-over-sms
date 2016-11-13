from transfer import strategy_list


class SendMessage:
    """Sends a message"""
    name = "SendMessage"
    description = "Sends a message"

    @staticmethod
    def execute(token):
        message = token.message

        # compose content
        correlationid = message.correlationid
        category = str(message.category)
        body = message.get_body()
        body_length = len(body)

        strategy = None
        for s in strategy_list:
            if s.is_supported(message.receiver):
                strategy = s
                break

        if strategy is None:
            raise Exception("No transfer-strategy is supported by reciever (id: {0}).".format(message.receiver.id))

        max_bodysize = strategy.max_bodysize
        if body_length > max_bodysize:
            bodies = [body[i:i + max_bodysize] for i in range(0, len(body), max_bodysize)]
            contents = [''.join([correlationid, category, str(position), body]) for position, body in enumerate(bodies)]

            strategy.send_multiple(message.receiver, contents)
        else:
            content = ''.join([correlationid, category, '0', body])
            strategy.send_single(message.receiver, content)
