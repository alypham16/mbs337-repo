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
"""
Example Output:

Chain A: 141 residues, 1069 atoms
Chain B: 146 residues, 1123 atoms
Chain C: 141 residues, 1069 atoms
Chain D: 146 residues, 1123 atoms

Requirements:

Use 4HHB.cif.

Use MMCIFParser from Bio.PDB.MMCIFParser to read the mmCIF file.

Remember the object hierarchy in Biopython PDB: structure → models → chains → residues → atoms. Use nested for loops to walk this hierarchy.

Only when the residue is non-hetero should you increment your residue counter and loop over its atoms to count them.

Match the example output format exactly.

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