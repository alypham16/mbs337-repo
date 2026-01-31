"""
Exercise Prompt:
Create a Python script called exercise3.py that:

1. Reads the input JSON file
2. Converts the data to XML format
3. Writes the output to a file called proteins.xml
"""

import json
import xmltodict

with open("protein_list.json", "r") as f:
    prot_data = json.load(f)

root = {}
root["protein_list"] = {"protein": prot_data["protein_list"]} # Creating a dictionary as a single root with the list inside a dictionary

with open ("proteins.xml", "w") as o:
    o.write(xmltodict.unparse(root, pretty = True))