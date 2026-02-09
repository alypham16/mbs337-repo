"""
Exercise Prompt:

Create a Python script called exercise4.py that:

1. Parses 4HHB.cif with MMCIFParser from Bio.PDB.
2. Iterates over the full structure hierarchy (all models, all chains).

For each chain, prints:
1. Chain ID
2. Number of non-hetero-residues in that chain
3. Number of atoms in the non-hetero-residues in that chain
"""

from Bio.PDB import MMCIFParser
parser = MMCIFParser()
with open("4HHB.cif", "r") as f:
    structure = parser.get_structure("4HHB", f)

for model in structure:
    for chain in model:
        chain_id = chain.get_id()
        residue_count = 0
        atom_count = 0
        for residue in chain:
            hetfield, resseq, icode = residue.get_id()
            if hetfield != " ":
                continue # skipping hetero residues
            residue_count += 1
            for atom in residue:
                atom_count += 1
        
        print(f"Chain {chain_id}: {residue_count} residues, {atom_count} atoms")