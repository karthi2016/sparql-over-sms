package org.sparqloversms.algorithm.reasoning.models;

import org.apache.jena.rdf.model.Model;

import java.util.HashMap;

public class ReasonerResult {

    private HashMap<String, Integer> tracker;
    private Model output;

    public ReasonerResult() {
        tracker = new HashMap<>();
    }

    /*-----------------------------------------------------------------------*/

    public HashMap<String, Integer> getTracker() {
        return tracker;
    }

    public void track(String name) {
        tracker.put(name, tracker.getOrDefault(name, 1));
    }

    public Model getOutput() {
        return output;
    }

    public void setOutput(Model output) {
        this.output = output;
    }
}
