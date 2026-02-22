# Homework 06

This directory is for homework 6 of MBS 337, Research Computing in Biology.

## Setup

The tools built for this exercise using Docker include logging and relevant command-line parameters. The image from Docker Hub can be pulled using the following:

```bash
docker pull alypham16/my_bio_tools:1.0

```
The image may also be built using the following command:
``` bash
git clone https://github.com/alypham16/mbs337-repo/
cd homework06
docker build -t homework06-scripts .
```

The following default files were used for this homework:

- immune_proteins.fasta: https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/immune_proteins.fasta.gz

- same1_rawReads.fastq: https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/sample1_rawReads.fastq.gz

- 4HHB.cif (hemoglobin structure): https://files.rcsb.org/download/4HHB.cif.gz

To run the tools, mount the "\$PWD" data directory (has input files and where output files will be written) to a directory in the container via /data using -v and run each script as your user using -u\$(id - u):\$(id -g)

The four files may be ran using the following example commands or user-specified parameters in place of them, with default settings included for thresholds:

- fasta_stats.py
    - "-i", "--input": a protein FASTA file 
    - "-o", "--output": an output file with select protein statistics (total number of sequences, residue total, largest 
        and shortest accessions)
    - example:
```bash
docker run --rm -u $(id -u):$(id -g) -v $(pwd):/data homework06-scripts \
python /code/fasta_stats.py -i /data/immune_proteins.fasta -o /data/immune_proteins_stats.txt
```

- fasta_filter.py: 
    - "-i", "--input": a protein FASTA file 
    - "-o", "--output": an output file with proteins with a sequence length surpassing the user-specified threshold
    - "-t", "--threshold": a minimum sequence length to filter proteins for the output FASTA file (default: 1000)
    - example:
```bash
docker run --rm -u $(id -u):$(id -g) -v $(pwd):/data homework06-scripts \
python /code/fasta_filter.py -i /data/immune_proteins.fasta -o /data/long_only.fasta -m 1000
```

- fastq_filter.py: 
    - "-i", "--input": a FASTQ file
    - "-o", "--output": a FASTQ file with a Phred score over the user-specified threshold
    - "-t", "--threshold": a minimum Phred score to filter proteins by (default: 30)
    - "-ec", "--encoding": a FASTQ file encoding (default: fastq-sanger)
    - example:   
```bash
docker run --rm -u $(id -u):$(id -g) -v $(pwd):/data homework06-scripts \
python /code/fastq_filter.py -i /data/sample1_rawReads.fastq -o /data/sample1_cleanReads.fastq -t 30 -e fastq-sanger
```

- mmcif_summary.py:
    - "-i", "--input": a path to input mmCIF file
    - "-o", "--output": a path to output JSON file
    - example:
```bash
docker run --rm -u $(id -u):$(id -g) -v $(pwd):/data homework06-scripts \
python /code/mmcif_summary.py -i /data/4HHB.cif -o /data/4HHB_summary.json
```

After running the container, the following files should be returned or created in your local working directory, given default setting names:

- immune_proteins_stats.txt: from fasta_stats.py, provides select summary statistics of input protein file.

- long_only.fasta: from fasta_filter, provides all sequences that meet the length threshold specified from the Docker command.

- sample1_cleanReads.fastq: from fastq_filter, provides high-quality FASTQ reads based on the user-specified threshold.

- 4HHB_summary.json: from 44HB.cif, provides the chain/residue summary from mmCIF in a JSON format. 


## Exercise Descriptions 

This homework is composed of 5 parts (https://mbs-337-sp26.readthedocs.io/en/latest/homework/homework06.html).

1. Rewriting the above scripts to containerize, separated into four different exercises that have similar functions as their original script files from Homeworks 4 and 5 with some additional requirements for containerization. 

2. Building a Dockerfile to containerize these newly modified files.

3. Runnings each script using docker run from outside the container.

4. Pushing the container to Docker Hub.

5. Building a README.md, this file.

## Miscellaneous
The following non-exercise files are also in the Git directory
- README.md: This file, which contains an overview of the homework06 directory.

- output_files: a sub-directory that includes 4HHB_summary.json, immune_proteins_stats.txt, long_only.fasta, and sample1_cleanReads.fastq.

To ensure optimal usage of the container:
- Run with -u \\$(id -u):$(id -g) to run the container with the ubuntu user ID to ensure output files are owned by you.

- Mount data folder using -v $(pwd):/data.

## AI Usage

No AI was used for this assignment.