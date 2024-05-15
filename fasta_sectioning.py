import sys
import random
import os
from Bio import SeqIO

# Split the fasta file into n sections
def split_fasta(fasta_file):
    # Read all records from the fasta file into a list
    records = list(SeqIO.parse(fasta_file, "fasta"))

    # Choose a random divisor as the number of sections from this interval
    n = 50

    # Calculate the size of each section
    section_size = len(records) // n

    # Get the base name of the input file (without the directory part)
    base_name = os.path.basename(fasta_file)

    # Split the records into sections
    for i in range(n):
        start = i * section_size
        if i == n - 1:  # Last section includes any leftover records
            end = len(records)
        else:
            end = start + section_size
        section = records[start:end]

    # Write the section to a new fasta file
        with open(f"/home/wout/xtandem/sectioning/SIHUMI_DB1_UNIPROT_50_2/{base_name}_{i+1}_{n}.fasta", "w") as output_handle:
            SeqIO.write(section, output_handle, "fasta")    

# Make the function executable from command line
if __name__ == "__main__":
    fasta_file = sys.argv[1]
    split_fasta(fasta_file)