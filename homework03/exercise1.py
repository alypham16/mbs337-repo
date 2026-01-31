"""
Exercise Prompt: Create a Python script called exercise 1.py that:

1. Defines a ProteinEntry model with Pydantic
2. Reads in the input JSON file as a Python Dictionary
3. Converts the Python Dictionary into a list of ProteinEntry objects

Then,

1. Write a function called find_total_mass() that prints the total combined 
mass of all proteins in the dataset.

2. Write a function called find_large_proteins() that prints a list of protein 
names of any proteins with a sequence length greater than or equal to 1000.

3. Write a function called find_non_eukaryotes() that prints a list of protein 
names of any non-eukaryotic proteins in the dataset. (Hint: A protein is considered 
non-eukaryotic if “Eukaryota” does not appear in protein.organism['lineage'])

After defining your functions, call each one so the results are printed to the 
terminal when the script runs.

"""
import json
from pydantic import BaseModel

with open("protein_list.json", "r") as f:
    prot_data = json.load(f)

class ProteinEntry(BaseModel): # template describing structure of any protein entry
    primaryAccession: str
    organism: dict
    proteinName: str
    sequence: dict
    geneName: str

proteins = []

for prot in prot_data["protein_list"]:
    proteins.append(ProteinEntry(**prot)) # unpacking dictionary to turn into ProteinEntry object

# Calculating the total mass of all proteins in the list
def find_total_mass(list_of_proteins) -> int:
    total_mass = 0
    for prot in proteins:
        total_mass += prot.sequence["mass"]
    print(total_mass)

# Finding proteins over 1000 amino acids long
def find_large_proteins(list_of_proteins) -> list:
    lg_prots = []
    for prot in proteins:
        if prot.sequence["length"] >= 1000:
            lg_prots.append(prot.proteinName)
    print(lg_prots)

# Finding non-eukaryotic proteins
def find_non_eukaryotes(list_of_proteins) -> list:
    non_eukarya = []
    for prot in proteins:
        if prot.organism["lineage"] != "Eukaryota":
            non_eukarya.append(prot.proteinName)
    print(non_eukarya)

find_total_mass(proteins)
find_large_proteins(proteins)
find_non_eukaryotes(proteins)
