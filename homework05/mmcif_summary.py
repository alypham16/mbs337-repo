"""
Exercise Prompt:

Create a Python script named mmcif_summary.py that:

1. Parses a mmCIF file (e.g., 4HHB.cif) using MMCIFParser from Bio.PDB.
2. For each chain in the structure, computes:
- total_residues — total number of residues in the chain
- hetero_residue_count — number of hetero residues (waters, ligands, ions, etc.)
- standard_residues — number of standard (non-hetero) residues
3. Writes the summary to a JSON file in the exact format 

"""
import json
from Bio.PDB import MMCIFParser

def extract_mmcif_info(structure) -> list:
    """
    Given a parsed MMCIF file, extracts the chain_id, total_residues,
    hetero_residue_count, and standard_residues for each chain and
    appends them to a list by iterating through each level and keeping 
    count of the respective information.

    Args:
        structure: a MMCIFParser object containing the protein information
    
    Returns:
        chains_lst: a list of all chains in the protein MMCIF file along with their
        chain_id, total_reisudes, standard_residues, and hetero_residue_count.
    """

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



final_44HB = {
    "chains" : chains_lst
}

def mmcif_to_json(mmcif_dict: dict) -> None:
    """
    Given a nested dictionary formatted with the contents from the mmcif_file,
    writes the appropriate json file.

    Args:
        mmcif_dict: a dictionary object containing the chain_id, total_residues, standard_residues, and hetero_residue count for each chain
    
    Returns:
        None (output JSON file to disk)
    """

    with open("44HB_summary.json", "w") as out:
        json.dump(final_44HB, out, indent=2)

def main():
    # Create parser, open file, create structure object, call summarize_chains()
    parser = MMCIFParser()
    with open("4HHB.cif", "r") as f:
        structure = parser.get_structure("4HHB", f)

    summarize_chains(structure)

if __name__ == "__main__":
    main()
