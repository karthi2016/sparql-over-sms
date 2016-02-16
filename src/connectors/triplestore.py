from SPARQLWrapper import SPARQLWrapper


class SPARQLConnector:
    """Connector used for performing SPARQL queries"""

    def __init__(self, config):
        self.config = config

    def insert(self, sub, pred, obj):
        sparql = SPARQLWrapper(self.config['endpoints']['update'])
        query = 'INSERT DATA {{ {0} {1} {2} }}'.format(sub, pred, obj)

        sparql.returnFormat = 'rdf+xml'
        sparql.method = 'POST'
        sparql.setQuery(query)
        sparql.query()

    def select(self, sub, pred, obj):
        sparql = SPARQLWrapper(self.config['endpoints']['query'])
        query = 'SELECT * WHERE {{ {0} {1} {2} }}'.format(sub, pred, obj)

        sparql.returnFormat = 'json'
        sparql.setQuery(query)
        return sparql.query().convert()
