package org.sparqloversms.compression.serialization;

import org.apache.jena.rdf.model.*;
import org.apache.jena.riot.Lang;
import org.apache.jena.riot.RDFDataMgr;
import org.apache.jena.vocabulary.RDF;
import org.topbraid.spin.arq.ARQ2SPIN;
import org.topbraid.spin.arq.ARQFactory;
import org.topbraid.spin.model.*;
import org.topbraid.spin.system.SPINModuleRegistry;

import org.apache.jena.query.Query;
import org.apache.jena.util.FileUtils;

import org.sparqloversms.compression.serialization.interfaces.Serializer;
import org.topbraid.spin.vocabulary.SP;

import java.io.*;
import java.util.HashMap;
import java.util.List;

public class SPINSerializer implements Serializer {

    public SPINSerializer() {
        SPINModuleRegistry.get().init();
    }

    /*-----------------------------------------------------------------------*/

    public String serialize(String input) {
        Model model = ModelFactory.createDefaultModel();
        Query query = ARQFactory.get().createQuery(model, input);

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

        return output;
    }

    private void shortenVariableNames(Model model) {
        Property varName = model.getProperty("http://spinrdf.org/sp#varName");
        Selector selector = new org.apache.jena.rdf.model.SimpleSelector(null, varName, null, "");
        List<Statement> statements = model.listStatements(selector).toList();

        int counter = 0;
        HashMap<String, String> mapping = new HashMap<>();
        for (Statement s : statements) {
            String name = s.getObject().asLiteral().toString();

            String replacement = mapping.getOrDefault(name, null);
            if (replacement == null) {
                replacement = String.valueOf(Character.toChars(97 + counter++));
                mapping.put(name, replacement);
            }

            s.changeObject(replacement);
        }
    }

    public String deserialize(String input) {
        Model model = ModelFactory.createDefaultModel();
        model.read(new StringReader(input), null, FileUtils.langTurtle);

        Model spinSchema = RDFDataMgr.loadModel("http://spinrdf.org/sp", Lang.RDFXML);
        InfModel infModel = ModelFactory.createRDFSModel(spinSchema, model);
        Resource queryInstance = SPINFactory.asQuery(infModel.listResourcesWithProperty(RDF.type, SP.Query).next());
        return SPINFactory.asQuery(queryInstance).toString();
    }
}
