# Homework 07

This directory is for homework 7 of MBS 337, Research Computing in Biology.

## Setup

The tools built for this exercise using Docker and Redis. The Redis container can be initiated using the following:

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
The Python script get_ncbi_genbank_records.py can be run using the following:

```bash
python get_ncbi_genbank_records.py
```

The four files may be ran using the following example commands or user-specified parameters in place of them, with default settings included for thresholds:

- get_ncbi_genbank_records.py
    - "-st", "--search": a search term to use for the protein database (defaults to Arabidopsis thaliana AND AT5G10140)
    - "-o", "--output": a name for the output file name (defaults to genbank_records.txt)
    - example:

```bash
python get_ncbi_genbank_records.py --output "genbank_records.txt"
```

After running the container, the following files should be returned or created in your local working directory, given default setting names:

- genbank_records.txt: a txt file of all the proteins that match the default criteria, "Arabidopsis thaliana AND AT5G10140."


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