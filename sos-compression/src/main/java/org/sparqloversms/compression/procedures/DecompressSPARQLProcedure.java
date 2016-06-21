package org.sparqloversms.compression.procedures;

import org.sparqloversms.compression.procedures.interfaces.Procedure;

public class DecompressSPARQLProcedure implements Procedure {
    private String input;
    private String knowledgeFile;

    public DecompressSPARQLProcedure(String input, String knowledgeFile) {
        this.input = input;
        this.knowledgeFile = knowledgeFile;
    }

    @Override
    public String start() {
        return input;
    }
}
