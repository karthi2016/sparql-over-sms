package org.sparqloversms.compression.serialization;

import org.apache.jena.rdf.model.InfModel;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.riot.Lang;
import org.apache.jena.riot.RDFDataMgr;
import org.apache.jena.vocabulary.RDF;
import org.topbraid.spin.arq.ARQ2SPIN;
import org.topbraid.spin.arq.ARQFactory;
import org.topbraid.spin.model.*;
import org.topbraid.spin.system.SPINModuleRegistry;

import org.apache.jena.query.Query;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.util.FileUtils;

import org.sparqloversms.compression.serialization.interfaces.Serializer;
import org.topbraid.spin.vocabulary.SP;

import java.io.*;

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

    public String deserialize(String input) {
        Model model = ModelFactory.createDefaultModel();
        model.read(new StringReader(input), null, FileUtils.langTurtle);

        Model spinSchema = RDFDataMgr.loadModel("http://spinrdf.org/sp", Lang.RDFXML);
        InfModel infModel = ModelFactory.createRDFSModel(spinSchema, model);
        Resource queryInstance = SPINFactory.asQuery(infModel.listResourcesWithProperty(RDF.type, SP.Query).next());
        return SPINFactory.asQuery(queryInstance).toString();
    }
}

//        String query =
//            "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema>\n" +
//            "PREFIX rm: <http://purl.org/collections/w4ra/radiomarche>\n" +
//            "\n" +
//            "CONSTRUCT {\n" +
//            "    ?adv rm:has_offering ?off .\n" +
//            "    ?adv rm:contact_tel ?tel .\n" +
//            "    ?off rdfs:label ?pname\n" +
//            "} WHERE {\n" +
//            "    ?off a rm:Offering .\n" +
//            "    ?off rm:has_contact ?contact .\n" +
//            "    ?off rm:prod_name ?prod.\n" +
//            "    ?prod rdfs:label ?pname.\n" +
//            "    ?adv rm:contact_tel ?tel .\n" +
//            "    ?adv rm:zone ?zone .\n" +
//            "    FILTER (?zone IN (rm:zone_Mafoune, rm:zone_Mandiakuy))\n" +
//            "}";
