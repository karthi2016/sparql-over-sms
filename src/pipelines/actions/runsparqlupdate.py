from SPARQLWrapper import SPARQLWrapper


class RunSparqlUpdate:
    """Runs a SPARQL update against a triple store"""
    name = "RunSparqlUpdate"
    description = "Runs a SPARQL update against a triple store"

    @staticmethod
    def execute(token):
        from webapi import app

        # initialize sparql endpoint
        sparql = SPARQLWrapper(app.config['c_triplestore']['endpoints']['update'])

        # prepare sparql update
        sparql.setQuery(token.message.body)
        sparql.method = 'POST'
        sparql.returnFormat = 'json'

        # return result un-altered
        token.result = sparql.query().convert()


