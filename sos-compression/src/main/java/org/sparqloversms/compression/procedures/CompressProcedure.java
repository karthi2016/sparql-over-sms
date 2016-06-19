package org.sparqloversms.compression.procedures;

import org.sparqloversms.compression.procedures.interfaces.Procedure;

public class CompressProcedure implements Procedure {
    private String inputFile;
    private String outputFile;

    public CompressProcedure(String inputFile, String outputFile) {
        this.inputFile = inputFile;
        this.outputFile = outputFile;
    }

    public void Start() {

    }
}
