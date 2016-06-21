package org.sparqloversms.compression;

import org.apache.commons.cli.*;
import org.apache.commons.io.FileUtils;
import org.sparqloversms.compression.procedures.CompressRDFProcedure;
import org.sparqloversms.compression.procedures.CompressSPARQLProcedure;
import org.sparqloversms.compression.procedures.DecompressRDFProcedure;
import org.sparqloversms.compression.procedures.DecompressSPARQLProcedure;
import org.sparqloversms.compression.procedures.interfaces.Procedure;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.logging.Logger;

public class CLI
{
    private static final Logger logger = Logger.getLogger(CLI.class.getName());
    private static Options options = new Options();
    private static CommandLineParser parser = new DefaultParser();

    public static void main( String[] args ) {
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
            if (hasCompress) {
                performCompression(type, inputFile, outputFile, knowledgeFile);
            }
            else {
                performDecompression(type, inputFile, outputFile, knowledgeFile);
            }
        } catch (ParseException | IllegalArgumentException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }

    private static void performCompression(String type, String inputFile, String outputFile, String knowledgeFile) {
        try {
            String input = FileUtils.readFileToString(new File(inputFile));

            // Pick the correct procedure for the job
            Procedure procedure;
            switch (type.toUpperCase()) {
                case "SPARQL":
                    procedure = new CompressSPARQLProcedure(input, knowledgeFile);
                    break;
                case "RDF":
                default:
                    procedure = new CompressRDFProcedure(input, knowledgeFile);
                    break;
            }

            String output = procedure.start();
            FileUtils.writeStringToFile(new File(outputFile), output);
        } catch (IOException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }

    private static void performDecompression(String type, String inputFile, String outputFile, String knowledgeFile) {
        try {
            String input = FileUtils.readFileToString(new File(inputFile));

            // Pick the correct procedure for the job
            Procedure procedure;
            switch (type.toUpperCase()) {
                case "SPARQL":
                    procedure = new DecompressSPARQLProcedure(input, knowledgeFile);
                    break;
                case "RDF":
                default:
                    procedure = new DecompressRDFProcedure(input, knowledgeFile);
                    break;
            }

            String output = procedure.start();
            FileUtils.writeStringToFile(new File(outputFile), output);
        } catch (IOException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
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
