"""
Exercise Prompt:

Create a Python script called exercise1.py that reads immune_proteins.fasta and prints:

1. The total number of sequences in the file
2. The total number of residues in the file
3. The accession ID and length of the longest sequence in the file

The accession ID and length of the shortest sequence in the file
"""

from Bio.SeqIO.FastaIO import SimpleFastaParser

total_sequences = 0
residue_total = 0
largest_sequence_len = 0
largest_sequence = ""
largest_sequence_residues = 0
shortest_sequence = ""
shortest_sequence_residues = float("inf")

with open("immune_proteins.fasta", "r") as f:
    for header, sequence in SimpleFastaParser(f):
        parts = header.split("|")
        total_sequences += 1
        residue_total += len(sequence)
        if len(sequence) > largest_sequence_residues:
            largest_sequence = parts[1]
            largest_sequence_residues = len(sequence)
        if len(sequence) < shortest_sequence_residues:
            shortest_sequence = parts[1]
            shortest_sequence_residues = len(sequence)

    print(f"Num Sequences: {total_sequences}")
    print(f"Total Residues: {residue_total}")
    print(f"Longest Accession: {largest_sequence} ({largest_sequence_residues} residues)")
    print(f"Shortest Accession: {shortest_sequence} ({shortest_sequence_residues} residues)")

