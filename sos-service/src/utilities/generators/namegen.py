from tempfile import _get_candidate_names


def generate_agent_name():
    name = next(_get_candidate_names())
    name = name.replace('_', '0')

    return '~{0}'.format(name)




