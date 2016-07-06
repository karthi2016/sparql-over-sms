package org.sparqloversms.algorithm.procedures;

import org.apache.jena.rdf.model.Model;
import org.sparqloversms.algorithm.encoding.interfaces.Decoder;
import org.sparqloversms.algorithm.encoding.model.DecoderResult;
import org.sparqloversms.algorithm.procedures.interfaces.DecompressionProcedure;
import org.sparqloversms.algorithm.procedures.models.DecompressionReport;
import org.sparqloversms.algorithm.serialization.interfaces.Deserializer;
import org.sparqloversms.algorithm.serialization.interfaces.Serializer;
import org.sparqloversms.algorithm.serialization.models.DeserializerResult;
import org.sparqloversms.algorithm.serialization.models.SerializerResult;

public class RDFDecompressionProcedure implements DecompressionProcedure {

    private Decoder decoder;
    private Deserializer deserializer;
    private Serializer serializer;

    public RDFDecompressionProcedure(Decoder decoder, Deserializer deserializer, Serializer serializer) {
        this.decoder = decoder;
        this.deserializer = deserializer;
        this.serializer = serializer;
    }

    @Override
    public DecompressionReport run(String procedureInput) {
        DecompressionReport report = new DecompressionReport();

        // Step 1 - decode
        String decoderInput = procedureInput;
        DecoderResult decoderResult = decoder.decode(decoderInput);
        report.setResult(decoderResult);

        // Step 2 - deserialize
        String deserializerInput = decoderResult.getOutput();
        DeserializerResult deserializerResult = deserializer.deserialize(deserializerInput);
        report.setResult(deserializerResult);

        // Step 3 - serialize
        Model serializerInput = deserializerResult.getOutput();
        SerializerResult serializerResult = serializer.serialize(serializerInput);
        report.setResult(serializerResult);

        return report.finish();
    }

}
