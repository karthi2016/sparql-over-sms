package org.sparqloversms.algorithm.procedures;

import org.sparqloversms.algorithm.encoding.HDTEncoder;
import org.sparqloversms.algorithm.encoding.interfaces.Encoder;
import org.sparqloversms.algorithm.procedures.interfaces.Procedure;
import org.sparqloversms.algorithm.serialization.SPINSerializer;
import org.sparqloversms.algorithm.serialization.interfaces.Serializer;
import java.io.IOException;

public class CompressSPARQLProcedure implements Procedure {
    private String input;
    private String knowledgeFile;

    public CompressSPARQLProcedure(String input, String knowledgeFile) {
        this.input = input;
        this.knowledgeFile = knowledgeFile;
    }

    @Override
    public String start() {
        try {
            // 1. Serialize to SPIN
            Serializer serializer = new SPINSerializer();
            String spin = serializer.serialize(input);

            // 2. Perform encoding
            Encoder encoder = new HDTEncoder(knowledgeFile);
            String output = encoder.encode(spin);

            return output;
        } catch (IOException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }

        return null;
    }
}
