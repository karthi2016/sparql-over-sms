package org.sparqloversms;

import org.apache.commons.cli.*;
import org.apache.commons.io.FileUtils;
import org.apache.commons.io.FilenameUtils;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.vocabulary.RDFS;
import org.apache.jena.vocabulary.VCARD;
import org.apache.log4j.BasicConfigurator;
import org.apache.log4j.varia.NullAppender;
import org.rdfhdt.hdt.hdt.HDT;
import org.rdfhdt.hdt.hdt.HDTManager;
import org.sparqloversms.algorithm.encoding.HDTDecoder;
import org.sparqloversms.algorithm.encoding.HDTEncoder;
import org.sparqloversms.algorithm.encoding.interfaces.Decoder;
import org.sparqloversms.algorithm.encoding.interfaces.Encoder;
import org.sparqloversms.algorithm.procedures.RDFCompressionProcedure;
import org.sparqloversms.algorithm.procedures.RDFDecompressionProcedure;
import org.sparqloversms.algorithm.procedures.SPARQLCompressionProcedure;
import org.sparqloversms.algorithm.procedures.SPARQLDecompressionProcedure;
import org.sparqloversms.algorithm.procedures.interfaces.DecompressionProcedure;
import org.sparqloversms.algorithm.procedures.interfaces.CompressionProcedure;
import org.sparqloversms.algorithm.procedures.models.CompressionReport;
import org.sparqloversms.algorithm.procedures.models.DecompressionReport;
import org.sparqloversms.algorithm.procedures.models.ProcedureReport;
import org.sparqloversms.algorithm.reasoning.RDFSReasoner;
import org.sparqloversms.algorithm.reasoning.interfaces.Reasoner;
import org.sparqloversms.algorithm.serialization.*;
import org.sparqloversms.algorithm.serialization.interfaces.Deserializer;
import org.sparqloversms.algorithm.serialization.interfaces.Serializer;

import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;

public class CLI {
    private static Options options = new Options();
    private static CommandLineParser parser = new DefaultParser();

    public static void main(String[] args) {
        defineOptions();

        // Temporary disable log4j (used by Jena)
        BasicConfigurator.configure(new NullAppender());

        try {
            CommandLine cmd = parser.parse(options, args);

            // Show help and stop, if --help is provided
            if (cmd.hasOption("help")) {
                showHelp();
            }

            // Validate if legal options and arguments are provided
            boolean hasCompress = cmd.hasOption("compress");
            boolean hasDecompress = cmd.hasOption("decompress");
            String type = cmd.getOptionValue("type");
            String inputFile = cmd.getOptionValue("input");
            String outputFile = cmd.getOptionValue("output");
            String knowledgeFile = cmd.getOptionValue("knowledge");
            String reportFile = cmd.getOptionValue("report");

            if (!hasCompress && !hasDecompress) {
                throw new ParseException("Either --compress or --decompress must be specified.");
            }
            if (hasCompress && hasDecompress) {
                throw new ParseException("The --compress and --decompress options are mutually exclusive.");
            }
            if (type == null) {
                throw new ParseException("The --type option is required.");
            }
            if (!type.toUpperCase().equals("SPARQL") && !type.toUpperCase().equals("RDF")) {
                throw new ParseException("The argument of the --type option must be either 'SPARQL' or 'RDF'.");
            }
            if (inputFile == null) {
                throw new ParseException("The --input option is required.");
            }
            if (knowledgeFile == null) {
                throw new ParseException("The --knowledge option is required.");
            }

            // Validate that the provided file paths are valid
            boolean inputFileExists = Files.exists(Paths.get(inputFile));
            boolean knowledgeFileExists = Files.exists(Paths.get(knowledgeFile));

            if (!inputFileExists) {
                throw new IllegalArgumentException("The input file cannot be found.");
            }
            if (!knowledgeFileExists) {
                throw new IllegalArgumentException("The knowledge file cannot be found.");
            }

            // All seems fine, let's do this
            HDT knowledge = readKnowledgeFile(knowledgeFile);

            ProcedureReport report;
            if (hasCompress) {
                Model input = readInputFileAsModel(inputFile, type);
                report = performCompression(type, input, knowledge);
            } else {
                String input = readInputFileAsText(inputFile);
                report = performDecompression(type, input, knowledge);
            }

            if (outputFile != null) {
                FileUtils.writeStringToFile(new File(outputFile), report.getOutput());
            } else {
                System.out.println(report.getOutput());
            }

            if (reportFile != null) {
                FileUtils.writeStringToFile(new File(reportFile), report.toJSON());
            }
        } catch (ParseException | IllegalArgumentException | IOException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }

    private static CompressionReport performCompression(String type, Model input, HDT knowledge) {
        Reasoner defaultReasoner = new RDFSReasoner(knowledge);
        Serializer defaultSerializer = new TurtleSerializer();
        Encoder defaultEncoder = new HDTEncoder(knowledge);

        CompressionProcedure procedure;
        if (type.toUpperCase().equals("RDF")) {
            procedure = new RDFCompressionProcedure(defaultReasoner, defaultSerializer, defaultEncoder);
        } else {
            Serializer spinSerializer = new SPINSerializer();
            procedure = new SPARQLCompressionProcedure(spinSerializer, defaultEncoder);
        }

        CompressionReport report = procedure.run(input);
        return report;
    }

    private static DecompressionReport performDecompression(String type, String input, HDT knowledge) {
        Decoder defaultDecoder = new HDTDecoder(knowledge);
        Deserializer defaultDeserializer = new TurtleDeserializer();
        Serializer defaultSerializer = new TurtleSerializer();

        DecompressionProcedure procedure;
        if (type.toUpperCase().equals("RDF")) {
            procedure = new RDFDecompressionProcedure(defaultDecoder, defaultDeserializer, defaultSerializer);
        } else {
            Deserializer spinDeserializer = new SPINDeserializer();
            Serializer sparqlSerializer = new SPARQLSerializer();

            procedure = new SPARQLDecompressionProcedure(defaultDecoder, spinDeserializer, sparqlSerializer);
        }

        DecompressionReport report = procedure.run(input);
        return report;
    }

    private static Model readInputFileAsModel(String inputFile, String type) {
        Model model = ModelFactory.createDefaultModel();

        if (type.toUpperCase().equals("SPARQL")) {
            try {
                byte[] encoded = Files.readAllBytes(Paths.get(inputFile));
                String sparql = new String(encoded, Charset.defaultCharset());

                return  model.add(VCARD.NOTE, RDFS.label, sparql);
            } catch (IOException e) {
                e.printStackTrace();
                System.exit(1);
            }
        }

        return model.read(inputFile);
    }

    private static String readInputFileAsText(String inputFile) {
        try {
            return FileUtils.readFileToString(new File(inputFile));
        } catch (IOException e) {
            e.printStackTrace();
            System.exit(1);
        }

        return null;
    }

    private static HDT readKnowledgeFile(String knowledgeFile) throws IOException {
        return HDTManager.loadHDT(knowledgeFile, null);
    }

    /* CLI helpers ----------------------------------------------------------*/

    private static void defineOptions() {
        options.addOption(Option.builder("h")
                .longOpt("help")
                .desc("shows help")
                .build()
        );

        OptionGroup commands = new OptionGroup();
        commands.isRequired();
        commands.addOption(Option.builder()
                .longOpt("compress")
                .desc("performs compression on input file")
                .build()
        );
        commands.addOption(Option.builder()
                .longOpt("decompress")
                .desc("performs decompression on input file")
                .build()
        );
        options.addOptionGroup(commands);

        options.addOption(Option.builder("i")
                .longOpt("input")
                .hasArg()
                .argName("file")
                .desc("absolute/relative path to input file")
                .build()
        );

        options.addOption(Option.builder("t")
                .longOpt("type")
                .hasArg()
                .argName("type")
                .desc("the type if the input: SPARQL or RDF")
                .build()
        );

        options.addOption(Option.builder("o")
                .longOpt("output")
                .hasArg()
                .argName("file")
                .desc("absolute/relative path to output file (.ttl)")
                .build()
        );

        options.addOption(Option.builder("k")
                .longOpt("knowledge")
                .hasArg()
                .argName("file")
                .desc("absolute/relative path to knowledge file (.hdt)")
                .build()
        );

        options.addOption(Option.builder("r")
                .longOpt("report")
                .hasArg()
                .argName("file")
                .desc("absolute/relative path to report file (.json)")
                .build()
        );
    }

    private static void showHelp() {
        HelpFormatter formatter = new HelpFormatter();
        formatter.printHelp("sos-compress", options, true);

        System.exit(0);
    }
}
