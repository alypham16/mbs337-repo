# Exercise Prompt: Using BioPython’s Seq class, determine the GC content of the following DNA sequence: 
# GAACCGGGAGGTGGGAATCCGTCACATATGAGAAGGTATTTGCCCGATAA

from Bio.Seq import Seq
dna_sequence = Seq("GAACCGGGAGGTGGGAATCCGTCACATATGAGAAGGTATTTGCCCGATAA")
for base in dna_sequence:
    g_content = dna_sequence.count("G")
    c_content = dna_sequence.count("C")
    gc_content = (g_content + c_content) / len(dna_sequence) * 100
print(gc_content)
