package org.sparqloversms.algorithm.encoding.model;

import java.util.HashMap;

public class DecoderResult {

    private String output;
    private HashMap<String, Integer> tracker;

    public DecoderResult() {
        tracker = new HashMap<>();
    }

    /*-----------------------------------------------------------------------*/

    public void track(String name) {
        Integer current = tracker.get(name);
        if (current == null) {
            current = 0;
        }

        tracker.put(name, current + 1);
    }

    public HashMap<String, Integer> getTracker() {
        return tracker;
    }

    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }

}
