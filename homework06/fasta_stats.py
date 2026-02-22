#!/usr/bin/env python3

import argparse
import logging
import socket
from Bio.SeqIO.FastaIO import SimpleFastaParser

# Logging setup
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
                    help = "Output protein stats file")

args = parser.parse_args()

format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)

logging.basicConfig(level = args.loglevel, format = format_str)

def extract_fasta_stats(input_file: object, output_file: object) -> None:
    """
    Given a protein fasta file, extracts the number of sequences, total number of residues,
    longest accession, and shortest accession and writes it into a txt file.

    Args:
        input_file (object): a FASTA file to extract statistical information from.
        output_file (object): a txt file that includes only the protein statistical 
        information requested (total number of sequences, residue total, largest 
        and shortest accessions)
    
    Returns:
        None
    """
    total_sequences = 0
    residue_total = 0
    largest_sequence_len = 0
    largest_sequence = ""
    largest_sequence_residues = 0
    shortest_sequence = ""
    shortest_sequence_residues = float("inf")

    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:

            logging.info(f"Extracting protein statistics from {input_file}")

            for header, sequence in SimpleFastaParser(infile):
                parts = header.split("|")
                total_sequences += 1
                residue_total += len(sequence)
                if len(sequence) > largest_sequence_residues:
                    largest_sequence = parts[1]
                    largest_sequence_residues = len(sequence)
                if len(sequence) < shortest_sequence_residues:
                    shortest_sequence = parts[1]
                    shortest_sequence_residues = len(sequence)

            outfile.write(f"Num Sequences: {total_sequences} \n")
            outfile.write(f"Total Residues: {residue_total} \n")
            outfile.write(f"Longest Accession: {largest_sequence} ({largest_sequence_residues} residues) \n")
            outfile.write(f"Shortest Accession: {shortest_sequence} ({shortest_sequence_residues} residues) \n")
        
    except FileNotFoundError as e:
        logging.error(f"Input fasta file not found.")
    
    except Exception as e:
        logging.error(f"Error: {e}")

def main():
    extract_fasta_stats(args.input, args.output)

if __name__ == "__main__":
    main()