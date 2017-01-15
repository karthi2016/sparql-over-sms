from rdflib import Graph


def convertrdf_bymimetype(rdf, mimetype):
    graph = Graph().parse(rdf, format='turtle')

    mimetype_mapping = {
        'text/turtle': 'turtle',
        'application/rdf+xml': 'pretty+xml',
        'application/ld+json': 'jsonld',
        'application/n-triples': 'nt',
        'text/n3': 'n3'
    }

    mimetype = mimetype[:mimetype.index(',')]
    rdf_format = mimetype_mapping.get(mimetype)
    converted = graph.serialize(format=rdf_format)

    return converted


