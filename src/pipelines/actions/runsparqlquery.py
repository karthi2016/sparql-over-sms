from SPARQLWrapper import SPARQLWrapper


class RunSparqlQuery:
    """Runs a SPARQL query against a triple store"""
    name = "RunSparqlQuery"
    description = "Runs a SPARQL query against a triple store"

    @staticmethod
    def execute(token):
        from webapi import app

        # initialize sparql endpoint
        sparql = SPARQLWrapper(app.config['c_triplestore']['endpoints']['query'])

        # prepare sparql update
        sparql.setQuery(token.message.body)
        sparql.method = 'GET'
        sparql.returnFormat = 'json'

        # return result un-altered
        token.result = sparql.query().convert()


