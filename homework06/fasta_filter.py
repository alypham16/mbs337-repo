#!/usr/bin/env python3

import argparse
import logging
import socket
from Bio.SeqIO.FastaIO import SimpleFastaParser

# Command line argument parsing

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--loglevel",
                    type = str,
                    required = False,
                    default = "WARNING",
                    help = "set log level to DEBUG, INFO, WARNING, ERROR, or CRITICAL")

parser.add_argument("-i", "--input", 
                    type = str,
                    required = True, 
                    help = "Input a FASTA file")

parser.add_argument("-o", "--output", 
                    type = str,
                    required = True, 
                    help = "Output FASTA clean reads file")

parser.add_argument("-t", "--threshold",
                    type = int,
                    required = True,
                    default = 1000,
                    help = "Minimum sequence length to include in output FASTA file (default: 1000)")

args = parser.parse_args()

# Logging setup

format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)

logging.basicConfig(level = args.loglevel, format = format_str)

# Core function

def long_filtering(input_file: object, output_file: object) -> None:
    """
    Given a FASTA file, filters out sequences that are shorter than a specified 
    threshold and writes the filtered sequences in a new FASTA file.

    Args:
        input_file: a FASTA file containing the sequences to be filtered.
        output_file: a FASTA file that includes only the sequences that are longer than the
        specified threshold.
        threshold: an integer specifying the minimum sequence length to include in the output file.

    Returns:
        None
    
    """
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            for header, sequence in SimpleFastaParser(infile):

                if len(sequence) >= args.threshold:
                    outfile.write(f">{header}\n")
                    outfile.write(f"{sequence}\n\n") # adding an extra line spacer in between for readibility
    
    except FileNotFoundError as e:
        logging.error(f"Input FASTA file not found: {e}")

    except Exception as e:
        logging.error(f"An error occurred while filtering sequences: {e}")

def main():
    long_filtering(args.input, args.output)

if __name__ == "__main__":
    main()

