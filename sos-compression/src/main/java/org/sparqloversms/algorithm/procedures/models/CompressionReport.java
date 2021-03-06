package org.sparqloversms.algorithm.procedures.models;

import com.alibaba.fastjson.serializer.PropertyFilter;
import org.sparqloversms.algorithm.encoding.model.EncoderResult;
import org.sparqloversms.algorithm.reasoning.models.ReasonerResult;
import org.sparqloversms.algorithm.serialization.models.SerializerResult;
import com.alibaba.fastjson.JSON;

import java.util.HashMap;

public class CompressionReport extends ProcedureReport {

    private long startTimestamp;
    private long finishTimestamp;

    private ReasonerResult reasonerResult;
    private SerializerResult serializerResult;
    private EncoderResult encoderResult;

    public CompressionReport() {
        this.startTimestamp = System.currentTimeMillis();

        // Empty placeholders
        reasonerResult = new ReasonerResult();
        serializerResult = new SerializerResult();
        encoderResult = new EncoderResult();
    }

    /*-----------------------------------------------------------------------*/

    public HashMap<String, Integer> getReasonerTracker() {
        return reasonerResult.getTracker();
    }

    public HashMap<String, Integer> getEncoderTracker() {
        return encoderResult.getTracker();
    }

    public void setResult(ReasonerResult reaonserResult) {
        this.reasonerResult = reaonserResult;
    }

    public void setResult(SerializerResult serializerResult) {
        this.serializerResult = serializerResult;
    }

    public void setResult(EncoderResult encoderResult) {
        this.encoderResult = encoderResult;
    }

    public long getDurationMillis() {
        if (finishTimestamp == 0) {
            return -1;
        }

        return finishTimestamp - startTimestamp;
    }

    public CompressionReport finish() {
        finishTimestamp = System.currentTimeMillis();
        return this;
    }

    public String getOutput() {
        return encoderResult.getOutput();
    }
}
