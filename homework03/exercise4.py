"""
Create a Python script called exercise4.py that:

1. Reads the uniprot_protein_list.json file
2. Converts the data to YAML format
3. Writes the output to a file called proteins.yaml
"""

import json
import yaml

with open("protein_list.json", "r") as f:
    prot_data = json.load(f)

with open("proteins.yaml", "w") as o:
    yaml.dump(prot_data, o, sort_keys = False, explicit_start = True, explicit_end = True)