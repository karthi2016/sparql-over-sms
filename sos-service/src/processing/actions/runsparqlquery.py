import rdflib
from SPARQLWrapper import SPARQLWrapper


class RunSparqlQuery:
    """Runs a SPARQL query against a triple store"""
    name = "RunSparqlQuery"
    description = "Runs a SPARQL query against a triple store"

    @staticmethod
    def execute(token):
        endpoint = "http://desktop-at8e6a4:3030/sos/query"

        # initialize sparql endpoint
        sparql = SPARQLWrapper(endpoint)

        # prepare sparql update
        sparql.setQuery(token.message.body)
        sparql.method = 'POST'
        sparql.returnFormat = 'application/rdf+xml'

        # return result un-altered
        result = sparql.query().convert()
        if type(result) is rdflib.ConjunctiveGraph:
            if len(result) <= 40:
                token.result = result.serialize(format='nt').decode('utf-8')
            else:
                token.result = result.serialize(format='turtle').decode('utf-8')
        else:
            token.result = result.toxml()

