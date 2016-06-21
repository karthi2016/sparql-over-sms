package org.sparqloversms.compression.procedures;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.rdf.model.impl.ModelCom;
import org.apache.jena.util.FileUtils;
import org.rdfhdt.hdt.hdt.HDT;
import org.rdfhdt.hdt.hdt.HDTManager;
import org.rdfhdt.hdtjena.HDTGraph;
import org.sparqloversms.compression.encoding.HDTEncoder;
import org.sparqloversms.compression.encoding.interfaces.Encoder;
import org.sparqloversms.compression.procedures.interfaces.Procedure;
import org.sparqloversms.compression.reasoning.RDFSReasoner;
import org.sparqloversms.compression.reasoning.interfaces.Reasoner;
import org.sparqloversms.compression.serialization.TurtleSerializer;
import org.sparqloversms.compression.serialization.interfaces.Serializer;
import java.io.IOException;
import java.io.StringReader;

public class CompressRDFProcedure implements Procedure {
    private String input;
    private String knowledgeFile;

    public CompressRDFProcedure(String input, String knowledgeFile) {
        this.input = input;
        this.knowledgeFile = knowledgeFile;
    }

    @Override
    public String start() {
        try {
            Model model = ModelFactory.createDefaultModel();
            try (final StringReader in = new StringReader(input)) {
                model.read( in, null, FileUtils.langNTriple);
            }

            // Load background knowlege file
            HDT hdt = HDTManager.loadIndexedHDT(knowledgeFile, null);
            Model knowledge = new ModelCom(new HDTGraph(hdt));

            // 1. Remove semantic redundancy from RDF
            Reasoner reasoner = new RDFSReasoner(knowledge);
            model = reasoner.removeRedundancy(model);

            // 2. Serialize to Turtle
            Serializer serializer = new TurtleSerializer();
            String turtle = serializer.serialize(model);

            // 2. Perform HDT(-based) encoding
            Encoder encoder = new HDTEncoder(hdt.getDictionary());
            String output = encoder.encode(turtle);

            return output;
        } catch (IOException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }

        return null;
    }
}
