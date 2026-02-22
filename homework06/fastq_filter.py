#!/usr/bin/env python3

import argparse
import logging
import socket
from Bio import SeqIO

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
                    help = "Input a FASTQ file")

parser.add_argument("-o", "--output", 
                    type = str,
                    required = True, 
                    help = "Output FASTQ clean reads file")

parser.add_argument("-ec", "--encoding", 
                    type = str,
                    required = False,
                    default = "fastq-sanger",
                    help = "FASTQ file encoding (default: fastq-sanger)")

parser.add_argument("-t", "--threshold",
                    type = int,
                    required = True,
                    default = 30,
                    help = "Minimum Phred score to include in output FASTQ file (default: 30)")    

args = parser.parse_args()

# Logging setup
format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)

logging.basicConfig(level = args.loglevel, format = format_str)


# Core function
def extract_quality_fastq(input_file: object, output_file: object) -> None:
    """
    Given a FASTQ file, filters out sequences that have an average Phred quality score
    below a specified threshold and writes the filtered sequences in a new FASTQ file.
    
    Args:
        input_file: a FASTQ file containing the sequences to be filtered.
        output_file: a FASTQ file that includes only the sequences that have an average 
        Phred quality score above the specified threshold.
        threshold: an integer specifying the minimum Phred score to include in the output file.

    Returns:
        None

    """
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            total_reads = 0
            passing_reads = 0
            for record in SeqIO.parse(infile, "fastq-sanger"):
                total_reads += 1
                average_phred = sum(record.letter_annotations["phred_quality"]) / len(record.letter_annotations["phred_quality"])
                if average_phred >= args.threshold:
                    SeqIO.write(record, outfile, "fastq-sanger")
                    passing_reads += 1

    except FileNotFoundError as e:
        logging.error(f"Input fasta file not found.")
    
    except Exception as e:
        logging.error(f"Error: {e}")


    logging.info(f"Total reads in original file: {total_reads}")
    logging.info(f"Reads passing filter: {passing_reads}")

def main():
    extract_quality_fastq(args.input, args.output)

if __name__ == "__main__":
    main()
