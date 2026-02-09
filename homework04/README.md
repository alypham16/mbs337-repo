# Homework 04

This directory is for homework 4 of MBS 337, Reserach Computing in Biology.

## Setup

The exercises for Homework 04 were ran in a virtual environment with the **biopython** package installed:

```bash
source myenv/bin/activate
pip3 install biopython
```

The following files were used for this homework:

- immune_proteins.fasta: https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/immune_proteins.fasta.gz (Exercises 1 and 2)
- sample1_rawReads.fastq: https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/sample1_rawReads.fastq.gz (Exercise 3)
- 4HHB.cif (hemoglobin structure): https://files.rcsb.org/download/4HHB.cif.gz (Exercise 4)

## Exercise Descriptions

All exercises require installation of the **biopython** package.

### Exercise 1

Reads immune_proteins.fasta and prints

1. The total number of sequences in the file
2. The total number of residues in the file
3. The accession ID and length of the longest sequence in the file

### Exercise 2

Reads immune_proteins.fasta and creates a FASTA file called long_only.fasta, which contains only sequences longer than or equal to 1000 residues.

### Exercise 3

Reads sample1_rawReads.fastq and
1. Keeps only reads with a Phred quality of at least 30.
2. Writes the filtered reads to a new FASTQ file called sample1_cleanReads.fastq
3. Prints the total number of reads in the original file and the number of reads that passed the filtration.

### Exercise 4

Parses 4HHB.cif with MMCIFParser to print the Chain ID, number of non-hetero-residues in that chain, and the number of atoms in the non-hetero-residues in that chain

## Miscellaneous
The following non-exercise files are also in the directory
- README.md: This file, which contains an overview of the homework04 directory
- output_files: a sub-directory that includes long_only.fasta and sample1_cleanReads.fastq for Exercises 2 and 3, respectively.

## AI Usage

No AI was used for this assignment.