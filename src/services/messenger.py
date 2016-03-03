
# message categories
SYSTEM = 0
SYSTEM_RESPONSE = 1
SPARQL_QUERY = 2
SPARQL_QUERY_RESPONSE = 3
SPARQL_UPDATE = 4
SPARQL_UPDATE_RESPONSE = 5


class Messenger:
    """Proxy for messaging"""
    categories = {
        SYSTEM: 'system',
        SYSTEM_RESPONSE: 'system-response',
        SPARQL_QUERY: 'sparql-query',
        SPARQL_QUERY_RESPONSE: 'sparql-query-response',
        SPARQL_UPDATE: 'sparql-update',
        SPARQL_UPDATE_RESPONSE: 'sparql-update-response'
    }
