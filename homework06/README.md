# Homework 06

This directory is for homework 6 of MBS 337, Research Computing in Biology.

## Setup

The exercises for Homework 06 were ran in a virtual environment with the **biopython** package installed prior to running them on the command line using Docker commands:

```bash
source myenv/bin/activate
pip3 install biopython
```

The following file was used for this homework:

- immune_proteins.fasta: https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/immune_proteins.fasta.gz

- same1_rawReads.fastq: https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/sample1_rawReads.fastq.gz

- 4HHB.cif (hemoglobin structure): https://files.rcsb.org/download/4HHB.cif.gz

## Exercise Descriptions 

This homework is composed of 4 parts. (https://mbs-337-sp26.readthedocs.io/en/latest/homework/homework06.html)

1. Rewriting the above scripts to containerize, separated into four different exercises that have similar functions as their original script files from Homeworks 4 and 5 with some additional requirements for containerization. 

2. Building a Dockerfile to containerize these newly modified files.

3. Runnings each script using docker run from outside the container.

4. Pushing the container to Docker Hub.

## Miscellaneous
The following non-exercise files are also in the directory
- README.md: This file, which contains an overview of the homework06 directory.

- output_files: a sub-directory that includes 4HHB_summary.json, immune_proteins_stats.txt, long_only.fasta, and sample1_cleanReads.fastq.

## AI Usage

No AI was used for this assignment.