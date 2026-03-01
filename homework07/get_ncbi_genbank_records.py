#!/usr/bin/env python3

from Bio import Entrez, SeqIO
import json
import argparse
import logging
import socket
import redis

# Command line argument parsing

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--loglevel",
                    type = str,
                    required = False,
                    default = "WARNING",
                    help = "set log level to DEBUG, INFO, WARNING, ERROR, or CRITICAL")

parser.add_argument("-o", "--output", 
                    type = str,
                    required = True, 
                    default = "genbank_records.txt",
                    help = "Input an output file name")

parser.add_argument("-st", "--search",
                    type = str,
                    required = False, 
                    default = "Arabidopsis thaliana AND AT5G10140",
                    help = "Input a search term for NCBI GenBank")

args = parser.parse_args()

# Logging setup

format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)

logging.basicConfig(level = args.loglevel, format = format_str)

# Core function

def entrez_search(search_term: str, retmax: int = 30) -> list:
    """
    Given a search term, searches the NCBI Protein database and 
    retrieves a list of GenBank records.

    Args:
        search_term (str): The search term to query NCBI GenBank.
        retmax (int): The maximum number of records to retrieve. Default set to 30.
    
    Returns:
        records (list): A list of GenBank records matching the search term.
    """
    logging.info(f"Searching NCBI Protein Database for term: {search_term} with retmax: {retmax}")

    Entrez.email = "A.N.Other@example.com"

    try:
        with Entrez.esearch(db = "protein", term = search_term, retmax = retmax) as h:
            gi_list = Entrez.read(h)["IdList"]

        with Entrez.efetch(db = "protein", id = gi_list, rettype = "gb", retmode = "text") as h:
            records = list(SeqIO.parse(h, "genbank"))

        logging.info(f"Successfully retrieved {len(records)} from the database.")
        return records
    
    except Exception as e:
        logging.error(f"An error occurred with fetching the records: {e}")
        return []


def record_files(records: list, output_file: str) -> None:
    """
    Given a list of GenBank records, prepares the list by converting
    the records in Redis as JSON and then writes the records to a text file.

    Args:
        records (list): A list of GenBank records.
        output_file (str): The name of the output file to write the records to.
    
    Returns:
        None
    """
    logging.info(f"Writing {len(records)} records to {output_file}")
    r = redis.Redis(host='localhost', port=6379, db=0)

    try:
        for record in records:
            record_data = {
                "id": record.id,
                "name": record.name,
                "description": record.description,
                "sequence": str(record.seq)
            }
            r.set(record.id, json.dumps(record_data))
    except Exception as e:
        logging.error(f"An error occurred while processing record {record.id}: {e}")

    try:
        with open("genbank_records.txt", "w") as outfile:
            for record in records:
                outfile.write(f"ID:{record.id}\nName:{record.name}\nDescription:{record.description}\nSequence:{record.seq}\n")
    except Exception as e:
        logging.error(f"An error occurred while trying to write the output file: {e}")

def main():
    records = entrez_search(args.search)
    record_files(records, args.output)

if __name__ == "__main__":
    main()