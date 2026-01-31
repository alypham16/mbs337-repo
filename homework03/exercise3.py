"""
Exercise Prompt:
Create a Python script called exercise3.py that:

1. Reads the input JSON file
2. Converts the data to XML format
3. Writes the output to a file called proteins.xml

Requirements:
1. Import the xmltodict module
2. Remember that XML requires exactly one root element
3. Use the pretty=True option when writing XML for readability
"""

import json
import xmltodict

with open("protein_list.json", "r") as f:
    prot_data = json.load(f)

root = {}
root["protein_list"] = {"protein": prot_data["protein_list"]}

with open ("proteins.xml", "w") as o:
    o.write(xmltodict.unparse(root, pretty = True))