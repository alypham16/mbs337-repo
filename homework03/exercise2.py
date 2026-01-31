"""
Exerise Prompt:

Create a Python script called exercise2.py that:

1. Reads the input JSON file into a Python dictionary
2. Converts the data to CSV format with the following columns:
    primaryAccession
    proteinName
    geneName
    organism_scientificName (extract from nested organism object)
    sequence_length (extract from nested sequence object)
    sequence_mass (extract from nested sequence object)
    function

3. Writes the output to a file called proteins.csv

Use the csv module from Python’s standard library

Include a header row with flattened field names (using underscores to indicate nesting)

Iterate through entries and extract nested values to create each row

Write each flattened row to the CSV file
"""

import json
import csv

# Converting JSON file into a python dictionary
with open("protein_list.json", "r") as f:
    prot_data = json.load(f)

with open("proteins.csv", "w") as o:
    csv_writer = csv.writer(o)

    # Flattening field names
    header = ["primaryAccession",
              "proteinName",
              "geneName",
              "organism_scientificName",
              "sequence_length",
              "sequence_mass",
              "function"]
    csv_writer.writerow(header)

    # Iterating through the entries
    for protein in prot_data["protein_list"]:
        row = [
            protein["primaryAccession"],
            protein["proteinName"],
            protein["geneName"],
            protein["organism"]["scientificName"],
            int(protein["sequence"]["length"]),
            int(protein["sequence"]["mass"]),
            protein["function"]
        ]
        csv_writer.writerow(row)