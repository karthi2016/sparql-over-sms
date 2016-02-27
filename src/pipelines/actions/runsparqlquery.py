from SPARQLWrapper import SPARQLWrapper


class RunSparqlQuery:
    """Runs a SPARQL query against a triple store"""

    @staticmethod
    def execute(message):
        from webapi import app
        sparql = SPARQLWrapper(app.config['c_triplestore']['endpoints']['query'])

        # prepare sparql update
        sparql.setQuery(message.body)
        sparql.method = 'GET'
        sparql.returnFormat = 'json'

        # return result un-altered
        return sparql.query().convert()


