package org.sparqloversms.compression;

import org.apache.commons.cli.*;
import org.sparqloversms.compression.procedures.CompressProcedure;
import org.sparqloversms.compression.procedures.DecompressProcedure;
import org.sparqloversms.compression.procedures.interfaces.Procedure;
import org.sparqloversms.compression.serialization.SPINSerializer;
import org.sparqloversms.compression.serialization.interfaces.Serializer;

import java.util.logging.Level;
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

            boolean hasHelp = cmd.hasOption("help");
            boolean hasCompress = cmd.hasOption("compress");
            boolean hasDecompress = cmd.hasOption("decompress");
            String inputFile = cmd.getOptionValue("input");
            String outputFile = cmd.getOptionValue("output");
            String type = cmd.getOptionValue("type");

            if (hasHelp) {
                showHelp();
            }
            if (!hasCompress && !hasDecompress) {
                throw new ParseException("Either --compress or --decompress must be specified.");
            }
            if (hasCompress && hasDecompress) {
                throw new ParseException("The --compress and --decompress options are mutually exclusive.");
            }
            if (inputFile == null) {
                throw new ParseException("The --input option is required.");
            }
            if (outputFile == null) {
                throw new ParseException("The --output option is required.");
            }
            if (type == null) {
                throw new ParseException("The --type option is required.");
            }
            if (!type.toUpperCase().equals("SPARQL") && !type.toUpperCase().equals("RDF")) {
                throw new ParseException("The argument of the --type option must be either 'SPARQL' or 'RDF'.");
            }

            if (hasCompress) {
                performCompression(inputFile, outputFile);
            } else {
                performDecompression(inputFile, outputFile);
            }
        } catch (ParseException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }

    private static void performCompression(String inputFile, String outputFile) {
        Procedure procedure = new DecompressProcedure(inputFile, outputFile);
        procedure.Start();
    }

    private static void performDecompression(String inputFile, String outputFile) {
        Procedure procedure = new DecompressProcedure(inputFile, outputFile);
        procedure.Start();
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

        options.addOption(Option.builder("o")
                .longOpt("output")
                .hasArg()
                .argName("file")
                .desc("absolute or relative path to the output file")
                .build()
        );

        options.addOption(Option.builder("t")
                .longOpt("type")
                .hasArg()
                .argName("type")
                .desc("the type if the input: SPARQL or RDF")
                .build()
        );
    }

    private static void showHelp() {
        HelpFormatter formatter = new HelpFormatter();
        formatter.printHelp("sos-compress", options, true);

        System.exit(0);
    }
}
