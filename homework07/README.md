# Homework 07

This directory is for homework 7 of MBS 337, Research Computing in Biology.

## Setup

The tools built for this exercise using Docker and Redis. The Redis container can be initiated using the following:

The image may also be built using the following:

``` bash
git clone https://github.com/alypham16/mbs337-repo/
cd homework07
docker compose up -d
docker ps
```
To stop the container, use

```bash
docker compose down
```
The Python script get_ncbi_genbank_records.py can be run using

```
python get_ncbi_genbank_records.py
```

The four files may be ran using the following example commands or user-specified parameters in place of them, with default settings included for thresholds:

- get_ncbi_genbank_records.py
    - "-i", "--input": a protein FASTA file 
    - "-o", "--output": an output file with select protein statistics (total number of sequences, residue total, largest 
        and shortest accessions)
    - example:
```bash
docker run --rm -u $(id -u):$(id -g) -v $(pwd):/data homework06-scripts \
python /code/fasta_stats.py -i /data/immune_proteins.fasta -o /data/immune_proteins_stats.txt
```

After running the container, the following files should be returned or created in your local working directory, given default setting names:

- immune_proteins_stats.txt: from fasta_stats.py, provides select summary statistics of input protein file.

- long_only.fasta: from fasta_filter, provides all sequences that meet the length threshold specified from the Docker command.

- sample1_cleanReads.fastq: from fastq_filter, provides high-quality FASTQ reads based on the user-specified threshold.

- 4HHB_summary.json: from 44HB.cif, provides the chain/residue summary from mmCIF in a JSON format. 


## Exercise Descriptions 

This homework is composed of 2 parts (https://mbs-337-sp26.readthedocs.io/en/latest/homework/homework07.html).

1. Using docker compose to start a container.

2. Creating a Python script called get_ncbi_genbank_records.py that searches the NCBI protein database for the search term "Arabidopsis thaliana AND AT5G10140" that retrives the list of GI numbers for the matching records, retrives the GenBank records for that list, parses them, stores the records in Redis, and retrives the records from Redis to wrte into genbank_records.txt.

## Miscellaneous
The following non-exercise files are also in the Git directory
- README.md: This file, which contains an overview of the homework07 directory.

- output_files: a sub-directory that includes genbank_records.txt

## AI Usage

No AI was used for this assignment.