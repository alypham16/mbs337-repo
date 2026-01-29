# Exercise Prompt: Write a function that calculates the percentage of each base (A, T, G, C) in a DNA sequence. 
# The function should return a dictionary with bases as keys and percentages as values. 
# Test it with a sequence of your choice and print the results formatted to 2 decimal places.

def base_percentage(dna_sequence):
    percentages = {}
    dna_length = len(dna_sequence)
    for base in dna_sequence:
        if base == "A":
            percentages["A"] = round((dna_sequence.count("A") / dna_length) * 100, 2)
        elif base == "T":
            percentages["T"] = round((dna_sequence.count("T") / dna_length) * 100, 2)
        elif base == "G":
            percentages["G"] = round((dna_sequence.count("G") / dna_length) * 100, 2)
        else:
            percentages["C"] = round((dna_sequence.count("C") / dna_length) * 100, 2)
    print(percentages)

# Testing function with sample DNA sequence, randomly generated via bioinformatics.org

test_sequence = """
aggagaggttttcattctatgaattaacacgacggttagcgtagtacgagctccccggga
ctcgattcctatgaactgcgtatgaataaaaggtcccgcttcacaacttcatgcatagtc
gcaatcctatgaatattaaggtagtcgatgtccttttgacctctcactgtctccgtgttc
tcgaagttatatccacagagcgatcaaagtagcaggcgtcgcggccgtgcacagctgcga
cctctttctgacctacctgccgttcacgaacggagtctggatcgataatctggaatgtta
ccaggactcatacgcaacgacacgtacccgcgctcccccggcgctcctgaatatctcgag
tttacatcgttccgtcagtgaaagtcgctgacgtctgggccactagtccctttaccccct
atggctgcctggcgatgactgactcactgaaagttgggatgaaaactttacgtaagggcg
gcggtcaggcgcaatcgtgattatagccggcacaaccgagaaatgccggcctgcctttct
tctaaaccgattcaataagataacactccagcaaggctcggatagacctgaatatatttc
acgtggtgattactcgagcaatttacatctgcacccctaggacatttacggtgctgtagt
tcccgtggctttcgtcagataccacaattagagaaagctggggaaggataccacagagtc
tgtgagcgcatcggattgtgatcccccctctgagcgtggaacctagtcccctaattgcgt
taacgctgcgctagcagccgcgcaacagccactaaggacagagacgttacccttccgcgt
cccagcggtatcaagtttcagatgtagcttcatcatggtatgaacgtattttcctaaccc
cgtccactcgccgctacgggccgtacgcgaggtggaatgaaaagtgtcatcgtatccagc
ttccgcgccgttaacaccgatcgacttaggggtaagacgt
"""

base_percentage(test_sequence.upper().replace("\n",""))
