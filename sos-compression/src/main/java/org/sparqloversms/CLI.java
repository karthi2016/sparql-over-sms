package org.sparqloversms;

import org.apache.commons.cli.*;
import org.apache.commons.io.FileUtils;
import org.apache.commons.io.FilenameUtils;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.vocabulary.RDFS;
import org.apache.jena.vocabulary.SKOS;
import org.apache.jena.vocabulary.VCARD;
import org.rdfhdt.hdt.hdt.HDT;
import org.rdfhdt.hdt.hdt.HDTManager;
import org.sparqloversms.algorithm.encoding.HDTEncoder;
import org.sparqloversms.algorithm.encoding.interfaces.Encoder;
import org.sparqloversms.algorithm.procedures.RDFCompressionProcedure;
import org.sparqloversms.algorithm.procedures.SPARQLCompressionProcedure;
import org.sparqloversms.algorithm.procedures.interfaces.Procedure;
import org.sparqloversms.algorithm.procedures.models.ProcedureReport;
import org.sparqloversms.algorithm.reasoning.RDFSReasoner;
import org.sparqloversms.algorithm.reasoning.interfaces.Reasoner;
import org.sparqloversms.algorithm.serialization.SPINSerializer;
import org.sparqloversms.algorithm.serialization.TurtleSerializer;
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
        long start = System.currentTimeMillis();
        defineOptions();

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
            if (outputFile == null) {
                throw new ParseException("The --output option is required.");
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
            Model input = readInputFile(inputFile);
            HDT knowledge = readKnowledgeFile(knowledgeFile);

            String output;
            if (hasCompress) {
                output = performCompression(type, input, knowledge);
            } else {
                output = performDecompression(type, input, knowledge);
            }

            FileUtils.writeStringToFile(new File(outputFile), output);
        } catch (ParseException | IllegalArgumentException | IOException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }

        long finish = System.currentTimeMillis();
        System.out.println(finish - start);
    }

    private static String performCompression(String type, Model input, HDT knowledge) {
        Reasoner defaultReasoner = new RDFSReasoner(knowledge);
        Serializer defaultSerializer = new TurtleSerializer();
        Encoder defaultEncoder = new HDTEncoder(knowledge);

        Procedure procedure;
        if (type.toUpperCase().equals("RDF")) {
            procedure = new RDFCompressionProcedure(defaultReasoner, defaultSerializer, defaultEncoder);
        } else {
            Serializer spinSerializer = new SPINSerializer();
            procedure = new SPARQLCompressionProcedure(spinSerializer, defaultEncoder);
        }

        ProcedureReport report = procedure.run(input);
        return report.getOutput();
    }

    private static String performDecompression(String type, Model input, HDT knowledge) {
        throw new UnsupportedOperationException("Decompression is not yet supported.");
    }

    private static Model readInputFile(String inputFile) {
        Model model = ModelFactory.createDefaultModel();

        String extension = FilenameUtils.getExtension(inputFile);
        if (extension.toUpperCase().equals("SPARQL")) {
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
                .desc("performs compression on the input file")
                .build()
        );
        commands.addOption(Option.builder()
                .longOpt("decompress")
                .desc("performs decompression on the input file")
                .build()
        );
        options.addOptionGroup(commands);

        options.addOption(Option.builder("i")
                .longOpt("input")
                .hasArg()
                .argName("file")
                .desc("absolute or relative path to the input file")
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
                .desc("absolute or relative path to the output file (.ttl)")
                .build()
        );

        options.addOption(Option.builder("k")
                .longOpt("knowledge")
                .hasArg()
                .argName("file")
                .desc("absolute or relative path the the knowledge file (.rdf|.hdt)")
                .build()
        );
    }

    private static void showHelp() {
        HelpFormatter formatter = new HelpFormatter();
        formatter.printHelp("sos-compress", options, true);

        System.exit(0);
    }
}
