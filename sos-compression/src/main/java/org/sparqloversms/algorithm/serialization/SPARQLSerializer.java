package org.sparqloversms.algorithm.serialization;

import org.apache.jena.rdf.model.InfModel;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.riot.Lang;
import org.apache.jena.riot.RDFDataMgr;
import org.apache.jena.util.FileUtils;
import org.apache.jena.vocabulary.RDF;
import org.sparqloversms.algorithm.serialization.interfaces.Serializer;
import org.sparqloversms.algorithm.serialization.models.SerializerResult;
import org.topbraid.spin.model.SPINFactory;
import org.topbraid.spin.vocabulary.SP;

import java.io.StringReader;

public class SPARQLSerializer implements Serializer {

    @Override
    public SerializerResult serialize(Model model) {
        SerializerResult result = new SerializerResult();

        Model spinSchema = RDFDataMgr.loadModel("http://spinrdf.org/sp", Lang.RDFXML);
        InfModel infModel = ModelFactory.createRDFSModel(spinSchema, model);
        Resource queryInstance = SPINFactory.asQuery(infModel.listResourcesWithProperty(RDF.type, SP.Query).next());
        String sparql = SPINFactory.asQuery(queryInstance).toString();
        result.setOutput(sparql);

        return result;
    }
}
