package org.sparqloversms.compression.procedures;

import org.sparqloversms.compression.procedures.interfaces.Procedure;
import java.io.File;

public class CompressRDFProcedure implements Procedure {
    private String input;
    private String knowledgeFile;

    public CompressRDFProcedure(String input, String knowledgeFile) {
        this.input = input;
        this.knowledgeFile = knowledgeFile;
    }

    @Override
    public String start() {
        return input;
    }
}
