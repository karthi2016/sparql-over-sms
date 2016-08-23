
def extract_all(raw_message):
    metadata = extract_metadata(raw_message)
    body = extract_body(raw_message)

    return (metadata + (body,))


def extract_metadata(raw_message):
    correlationid = raw_message[:3]
    category = raw_message[3:4]
    position = raw_message[4:5]
    
    return (correlationid, category, position)


def extract_body(raw_message):
    return raw_message[5:]