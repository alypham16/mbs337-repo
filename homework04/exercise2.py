"""
Exercise Prompt:
Create a Python script called exercise2.py that reads immune_proteins.fasta 
using SimpleFastaParser again. This time, your script should write out a new 
FASTA file called long_only.fasta containing only the sequences longer than or 
equal to 1000 residues. Each output record must be a valid FASTA with the original 
headers format preserved.
"""

from Bio.SeqIO.FastaIO import SimpleFastaParser

with open("immune_proteins.fasta", "r") as infile, open("long_only.fasta", "w") as outfile:
    for header, sequence in SimpleFastaParser(infile):

        if len(sequence) >= 1000:
            outfile.write(f">{header}\n")
            outfile.write(f"{sequence}\n\n") # adding an extra line spacer in between for readibility
