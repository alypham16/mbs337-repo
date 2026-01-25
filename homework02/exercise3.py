# Exercise Prompt: Write a function that calculates the percentage of each base (A, T, G, C) in a DNA sequence. 
# The function should return a dictionary with bases as keys and percentages as values. 
# Test it with a sequence of your choice and print the results formatted to 2 decimal places.

def base_percentage(dna_sequence):
    percentages = {}
    dna_length = len(dna_sequence)
    for base in dna_sequence:
        if base == "A":
            percentages["A"] = (dna_sequence.count("A") / dna_length) * 100
        elif base == "T":
            percentages["T"] = (dna_sequence.count("T") / dna_length) * 100
        elif base == "G":
            percentages["G"] = (dna_sequence.count("G") / dna_length) * 100
        else:
            percentages["C"] = (dna_sequence.count("C") / dna_length) * 100
    return percentages

# Testing function with sample DNA sequence, via bioinformatics.org
test_sequence = 
"""
catcgatgatctgcggagcctgacgttcgtatacggggcagtagtgtactatggcgacgc
tcgctacgccgaagcttcgacgggttactttttatactggcctagtatgatcgaacgatg
tttccaccatgatcagacgatctagggtgtgtcatgttttcgacagatgcctctcatggt
gaaactactgaacattgggtatctaccttggttcggcccctattacacaaagccatgcgg
ctattccgctaatgtcgctactttaacccaacaatcagaaagtcccccatggacaaaagt
cggacctataataagttttgcagcgggccacctggtccacactccacaaatcactgccgc
atcagctagcaagaacggtatacaaatgctatgcggttctacggcactgggagtgaatac
ggagctttatcaaaatagctggttagggccccttaaagagcgctgacattacgatcgaca
gctctaactaacaacggcacgtgtgatactttcatcagagcctcttgcttcatatcggca
gtatctgacgtaggtgccttatagggataacgggttgcaccggggggtcccgatcgtaaa
cggccgaatcagtcaaacgcgcaggagcaagaataccctagtcccaggtgcggtatatga
cactcagttgctcgggtccaccgtcagacgaaagcagcagtgcccccgttccgtggcact
agccgaccgtactgagttcgatcctccgtacttcaaagtatttttggaccgtcatattac
taggctgacaaacggaaggactttgctaagtagagtcacaacgtgtggtgatgcgcatgt
gccgacgctacgtaattcgatgtacgactagtctctcagtcgcgcttcgctgatgaataa
gtagaaagcgtggaaactgtgttgaaagtatggatatgtgcaagccgcgataatgagtcg
atgtgcatcaacgtaccctacaaatgatccagtgtccaaacttggtgctggtggtggcagc
"""
base_percentages(test_sequence.replace("\n", ""))
            