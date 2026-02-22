import json
import argparse
import logging
import socket
from Bio.PDB import MMCIFParser


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
                    help = "Path to input mmCIF file")

parser.add_argument("-o", "--output",
                    type = str,
                    required = True,
                    help = "Path to output JSON file")

args = parser.parse_args()

# Logging setup

format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)

logging.basicConfig(level = args.loglevel, format = format_str)

# Core functions

def extract_mmcif_info(structure: object) -> list:
    """
    Given a parsed MMCIF file, extracts chain per-residue information.

    Args:
        structure: a parsed Bio.PDB object containing the protein information
        from an mmCIF file.
    
    Returns:
        chains_lst: a list of dictionaries, one per chain, with the following
        extracted information:
        - chain_id
        - total_residues
        - standard_residues
        - hetero_residue_count
    """
    logging.debug(f"Extracting residue information from {structure}")

    chains_lst = []
    for model in structure:
        for chain in model:
            chain_id = chain.get_id()
            total_residues = 0
            hetero_residue_count = 0
            standard_residues = 0
            for residue in chain:
                total_residues += 1
                hetfield, resseq, icode = residue.get_id()
                if hetfield != " ":
                    hetero_residue_count += 1
                else:
                    standard_residues += 1
            chains_lst.append({
                "chain_id": chain_id,
                "total_residues": total_residues,
                "standard_residues": standard_residues,
                "hetero_residue_count": hetero_residue_count
                    }) 
    return chains_lst

def mmcif_to_json_formatter(chains_lst: list) -> dict:
    """
    Given a list of per-chain information from a MMCIF file,
    adds them to a nested dictionary format for a specific
    JSON file format.

    Args:
        chains_lst: a list contianing a dictionary of each chain statistics.
    
    Returns:
        mmcif_dict: a nested dictionary formatted to the required JSON format.
    """

    mmcif_dict = {
        "chains" : chains_lst
    }
    
    return mmcif_dict

def mmcif_to_json(mmcif_dict: dict, outfile_file: str) -> None:
    """
    Given a nested dictionary formatted with the contents from the mmCIF dictionary,
    writes the appropriate JSON file.

    Args:
        mmcif_dict: a dictionary object containing the following for each chain:
        - chain_id
        - total_residues
        - standard_residues
        - hetero_residue_count
        outfile_file: a string containing the path to the output JSON file.
    
    Returns:
        None (output JSON file to disk)
    """

    with open(outfile_file, "w") as out:
        json.dump(mmcif_dict, out, indent = 2)

def main():
    # Create parser, open file, create structure object, call the required functions.
    
    cif_parser = MMCIFParser()

    try:
        structure = cif_parser.get_structure("structure", args.input)

        chains_lst = extract_mmcif_info(structure)
        mmcif_dict = mmcif_to_json_formatter(chains_lst)
        mmcif_to_json(mmcif_dict, args.output)

        logging.info("MMCIF file extraction and JSON file creation complete.")
    
    except FileNotFoundError as e:
        logging.error(f"Input mmCIF file not found: {e}")

    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()