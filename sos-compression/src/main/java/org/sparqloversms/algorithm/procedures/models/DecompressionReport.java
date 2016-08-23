package org.sparqloversms.algorithm.procedures.models;

import com.alibaba.fastjson.serializer.PropertyFilter;
import org.apache.jena.rdf.model.Model;
import org.sparqloversms.algorithm.encoding.model.DecoderResult;
import org.sparqloversms.algorithm.encoding.model.EncoderResult;
import org.sparqloversms.algorithm.reasoning.models.ReasonerResult;
import org.sparqloversms.algorithm.serialization.interfaces.Serializer;
import org.sparqloversms.algorithm.serialization.models.DeserializerResult;
import org.sparqloversms.algorithm.serialization.models.SerializerResult;
import com.alibaba.fastjson.JSON;

import java.util.HashMap;

public class DecompressionReport extends ProcedureReport {

    private long startTimestamp;
    private long finishTimestamp;

    private DecoderResult decoderResult;
    private DeserializerResult deserializerResult;
    private SerializerResult serializerResult;

    public DecompressionReport() {
        this.startTimestamp = System.currentTimeMillis();

        // Empty placeholders
        decoderResult = new DecoderResult();
        deserializerResult = new DeserializerResult();
        serializerResult = new SerializerResult();
    }

    /*-----------------------------------------------------------------------*/

    public HashMap<String, Integer> getDecoderTracker() {
        return decoderResult.getTracker();
    }

    public void setResult(DeserializerResult deserializerResult) {
        this.deserializerResult = deserializerResult;
    }

    public void setResult(DecoderResult decoderResult) {
        this.decoderResult = decoderResult;
    }

    public void setResult(SerializerResult serializerResult) {
        this.serializerResult = serializerResult;
    }

    public long getDurationMillis() {
        if (finishTimestamp == 0) {
            return -1;
        }

        return finishTimestamp - startTimestamp;
    }

    public DecompressionReport finish() {
        finishTimestamp = System.currentTimeMillis();
        return this;
    }

    public String getOutput() {
        return serializerResult.getOutput();
    }

    public String toJSON() {
        PropertyFilter filter = (source, name, value) -> !"output".equals(name);
        return JSON.toJSONString(this, filter);
    }
}
