package org.sparqloversms.compression.encoding;

import org.apache.jena.rdf.model.*;
import org.apache.jena.util.FileUtils;
import org.rdfhdt.hdt.dictionary.Dictionary;
import org.rdfhdt.hdt.enums.TripleComponentRole;
import org.rdfhdt.hdt.hdt.HDT;
import org.rdfhdt.hdt.hdt.HDTManager;
import org.sparqloversms.compression.encoding.interfaces.Encoder;
import java.io.IOException;
import java.io.StringReader;
import java.io.StringWriter;
import java.util.Map;

public class HDTEncoder implements Encoder {

    private Dictionary dictionary;

    public HDTEncoder(String hdtFileName) throws IOException {
        HDT hdt = HDTManager.loadHDT(hdtFileName, null);
        dictionary = hdt.getDictionary();
    }

    /*-----------------------------------------------------------------------*/

    public String encode(String input) {
        Model model = ModelFactory.createDefaultModel();
        String output;

        try {
            try (final StringReader in = new StringReader(input)) {
                model.read( in, null, FileUtils.langTurtle);
            }

            try(final StringWriter sw = new StringWriter())
            {
                model.write(sw, FileUtils.langTurtle);
                output = sw.toString();
            }
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }

        StmtIterator iter = model.listStatements();
        while (iter.hasNext()) {
            Statement triple = iter.nextStatement();

            Resource subject = triple.getSubject();
            Property predicate = triple.getPredicate();
            RDFNode object = triple.getObject();

            output = encodeSubject(subject, model, output);
            output = encodePredicate(predicate, model, output);
            output = encodeObject(object, model, output);
        }

        output = removeUnnecessaryPrefixes(model, output);

        // Remove double spaces and newlines to minimize output
        output = output.replace("\n", " ").replace("\r", " ");
        output = output.trim().replaceAll(" +", " ");
        return output;
    }

    private String encodeSubject(Resource subject, Model model, String output) {
        String value = subject.toString();
        int id = dictionary.stringToId(value, TripleComponentRole.SUBJECT);

        if (id != -1) {
            Map<String, String> map = model.getNsPrefixMap();
            for (Map.Entry<String, String> entry : map.entrySet()) {
                boolean match = value.startsWith(entry.getValue());
                if (match) {
                    value = value.replace(entry.getValue(), entry.getKey() + ":");
                    break;
                }
            }

            output = output.replaceAll(String.format("<?%s>?", value), String.format("\\$%x", id));
        }

        return output;
    }

    private String encodePredicate(Property predicate, Model model, String output) {
        String value = predicate.toString();
        int id = dictionary.stringToId(value, TripleComponentRole.SUBJECT);

        if (id != -1) {
            Map<String, String> map = model.getNsPrefixMap();
            for (Map.Entry<String, String> entry : map.entrySet()) {
                boolean match = value.startsWith(entry.getValue());
                if (match) {
                    value = value.replace(entry.getValue(), entry.getKey() + ":");
                    break;
                }
            }

            output = output.replaceAll(String.format("<?%s>?", value), String.format("\\$%x", id));
        }

        return output;
    }

    private String encodeObject(RDFNode object, Model model, String output) {
        if (object.isAnon()) {
            return output;
        }

        String value = (object.isLiteral() ? object.asLiteral() : object.asResource()).toString();
        int id = dictionary.stringToId(value, TripleComponentRole.SUBJECT);
        if (id != -1) {
            Map<String, String> map = model.getNsPrefixMap();
            for (Map.Entry<String, String> entry : map.entrySet()) {
                boolean match = value.startsWith(entry.getValue());
                if (match) {
                    value = value.replace(entry.getValue(), entry.getKey() + ":");
                    break;
                }
            }

            output = output.replaceAll(String.format("<?%s>?", value), String.format("\\$%x", id));
        }

        return output;
    }

    private String removeUnnecessaryPrefixes(Model model, String output) {
        Map<String, String> map = model.getNsPrefixMap();
        for (Map.Entry<String, String> entry : map.entrySet()) {
            String key = entry.getKey();
            String prefixPattern = String.format("<%s:", key);

            if (!output.contains(prefixPattern)) {
                output = output.replaceAll(String.format("@prefix %s: .*\\.", key), " ");
            }
        }

        return output;
    }
}
