
UNRECOGNIZED_ADDRESS = 'UA'
PHONENUMBER_ADDRESS = 'PA'
HOSTNAME_ADDRESS = 'HA'


def determine_address_type(address):
    if is_phonenumber_address(address):
        return PHONENUMBER_ADDRESS

    if is_hostname_address(address):
        return HOSTNAME_ADDRESS

    # not regocognized, default to hostname if..
    if ' ' not in address:
        return HOSTNAME_ADDRESS

    return UNRECOGNIZED_ADDRESS


def is_phonenumber_address(address):
    return address[0] == '+'


def is_hostname_address(address):
    characters = set(address)
    return ('.' in characters or ':' in characters) and ' ' not in characters
