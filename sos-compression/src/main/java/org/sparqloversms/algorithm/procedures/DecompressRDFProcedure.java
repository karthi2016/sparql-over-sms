package org.sparqloversms.algorithm.procedures;

import org.sparqloversms.algorithm.procedures.interfaces.Procedure;

public class DecompressRDFProcedure implements Procedure {
    private String input;
    private String knowledgeFile;

    public DecompressRDFProcedure(String input, String knowledgeFile) {
        this.input = input;
        this.knowledgeFile = knowledgeFile;
    }

    @Override
    public String start() {
        return input;
    }
}
