package org.sparqloversms.algorithm.serialization;

import org.apache.jena.rdf.model.*;
import org.apache.jena.riot.Lang;
import org.apache.jena.riot.RDFDataMgr;
import org.apache.jena.vocabulary.RDF;
import org.apache.jena.vocabulary.RDFS;
import org.apache.jena.vocabulary.VCARD;
import org.sparqloversms.algorithm.serialization.models.SerializerResult;
import org.topbraid.spin.arq.ARQ2SPIN;
import org.topbraid.spin.arq.ARQFactory;
import org.topbraid.spin.model.*;
import org.topbraid.spin.system.SPINModuleRegistry;

import org.apache.jena.query.Query;
import org.apache.jena.util.FileUtils;

import org.sparqloversms.algorithm.serialization.interfaces.Serializer;
import org.topbraid.spin.vocabulary.SP;

import java.io.*;
import java.util.HashMap;
import java.util.List;

public class SPINSerializer implements Serializer {

    public SPINSerializer() {
        SPINModuleRegistry.get().init();
    }

    /*-----------------------------------------------------------------------*/

    @Override
    public SerializerResult serialize(Model model) {
        SerializerResult result = new SerializerResult();

        RDFNode input = model.listObjectsOfProperty(VCARD.NOTE, RDFS.label).next();
        String sparql = input.asLiteral().toString();

        model = ModelFactory.createDefaultModel();
        Query query = ARQFactory.get().createQuery(model, sparql);

        ARQ2SPIN arq2SPIN = new ARQ2SPIN(model, true);
        arq2SPIN.createQuery(query, null);

        shortenVariableNames(model);

        String output = null;
        try(StringWriter sw = new StringWriter())
        {
            model.write(sw, FileUtils.langTurtle);
            output = sw.toString();

        } catch (IOException e) {
            e.printStackTrace();
        }

        result.setOutput(output);
        return result;
    }

    private void shortenVariableNames(Model model) {
        Property varName = model.getProperty("http://spinrdf.org/sp#varName");
        Selector selector = new org.apache.jena.rdf.model.SimpleSelector(null, varName, null, "");
        List<Statement> statements = model.listStatements(selector).toList();

        int counter = 0;
        HashMap<String, String> mapping = new HashMap<>();
        for (Statement s : statements) {
            String name = s.getObject().asLiteral().toString();

            String replacement = mapping.get(name);
            if (replacement == null) {
                replacement = String.valueOf(Character.toChars(97 + counter++));
                mapping.put(name, replacement);
            }

            s.changeObject(replacement);
        }
    }
}
