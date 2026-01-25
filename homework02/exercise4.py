# You are analyzing gene expression data from an RNA-seq experiment comparing control and treatment conditions. 
# You have measured expression levels for three different genes, with three biological replicates per condition. 
# Create a dictionary to store expression data for 3 genes, where each gene has control and treatment values as follows:

# Gene 1: Control values = 10.5, 11.2, 10.8; Treatment values = 25.3, 24.7, 26.1
# Gene 2: Control values = 8.2, 8.5, 8.0; Treatment values = 12.1, 11.8, 12.5
# Gene 3: Control values = 15.0, 14.8, 15.2; Treatment values = 18.5, 18.2, 18.8

# Then, write a script that:

# Calculates the mean expression for control and treatment for each gene
# Calculates the fold change (treatment mean/control mean) for each gene
# Prints the results, and identifies which genes show significant changes (use a threshold of fold change > 2.0 OR fold change < 0.5)

genes = {"Gene 1": {"Control": [10.5, 11.2, 10.8], "Treatment": [25.3, 24.7, 26.1]},
         "Gene 2": {"Control": [8.2, 8.5, 8.0], "Treatment": [12.1, 11.8, 12.5]},
         "Gene 3": {"Control": [15.0, 14.8, 15.2], "Treatment": [18.5, 18.2, 18.8]}}

for gene, data in genes.items():
    