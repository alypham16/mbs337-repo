"""
Exercise Prompt:

Create a Python script called exercise3.py that:

1. Reads sample1_rawReads.fastq using SeqIO.parse with the correct format.
2. Keeps only reads whose average Phred quality is at least 30.
3. Writes those filtered reads out to a new FASTQ file named sample1_cleanReads.fastq.
4. Prints to the terminal the total number of reads in the original file and the number 
of reads that passed quality control.
"""

from Bio import SeqIO
with open("sample1_rawReads.fastq", "r") as infile, open("sample1_cleanReads.fastq", "w") as outfile:
    total_reads = 0
    passing_reads = 0
    for record in SeqIO.parse(infile, "fastq-sanger"):
        total_reads += 1
        average_phred = sum(record.letter_annotations["phred_quality"]) / len(record.letter_annotations["phred_quality"])
        if average_phred >= 30:
            SeqIO.write(record, outfile, "fastq-sanger")
            passing_reads += 1

print(f"Total reads in original file: {total_reads}")
print(f"Reads passing filter: {passing_reads}")
