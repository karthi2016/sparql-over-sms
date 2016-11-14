package org.sparqloversms.algorithm.serialization.models;

import org.apache.jena.rdf.model.Model;

public class DeserializerResult {

    private Model output;

    public DeserializerResult() {

    }

    /*-----------------------------------------------------------------------*/

    public Model getOutput() {
        return output;
    }

    public void setOutput(Model output) {
        this.output = output;
    }


}
