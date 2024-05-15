import sys
import os
from psm_utils.io.xtandem import XTandemReader
from Bio import SeqIO
import random

# Function to extract protein IDs from an XML file
def extract_protein_ids_from_xml(xml_file):
    # Use the XTandemReader to read the XML file
    reader = XTandemReader(xml_file)
    # Extract the PSMs
    psm_list = reader.read_file()
    # Turn psm_list into dataframe
    psm_list = psm_list.to_dataframe()
    # Extract the protein IDs
    protein_ids = psm_list['protein_list'].tolist()
    protein_ids = [list(item) for item in dict.fromkeys(tuple(sublist) for sublist in protein_ids)]
    return protein_ids

# Function to extract protein sequences from a FASTA file
def extract_sequences_from_fasta(fasta_file, protein_ids):
    # Parse the FASTA file and create a dictionary that maps protein IDs to sequences
    sequences = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))
    # Extract the sequences of the identified proteins
    identified_sequences = {protein_id: sequences[protein_id] for protein_id in protein_ids if protein_id in sequences}
    return identified_sequences

# Function to write protein sequences to a FASTA file
def write_sequences_to_fasta(identified_sequences, output_file):
    # Write the sequences to the output file
    SeqIO.write(identified_sequences.values(), output_file, "fasta")

# Main function
def main(xml_dir, fasta_file, output_file):
    # Initialize an empty set to store all protein IDs
    all_protein_ids = set()
    # Loop over all XML files in the directory
    for xml_file in os.listdir(xml_dir):
        if xml_file.endswith(".xml"):
            # Extract protein IDs from the XML file and add them to the set
            protein_ids = extract_protein_ids_from_xml(os.path.join(xml_dir, xml_file))
            # Flatten the list of protein IDs
            protein_ids = [item for sublist in protein_ids for item in sublist]
            # Add the protein IDs to the set
            all_protein_ids.update(protein_ids)
    # Extract the sequences of the identified proteins from the FASTA file
    identified_sequences = extract_sequences_from_fasta(fasta_file, all_protein_ids)
    # Write the sequences of the identified proteins to the output file
    write_sequences_to_fasta(identified_sequences, output_file)

    # Parse the FASTA file and create a dictionary that maps protein IDs to sequences
    all_sequences = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))
    # Remove the identified sequences from the dictionary
    for protein_id in all_protein_ids:
        all_sequences.pop(protein_id, None)
    # Select a random sample of sequences
    random_sequences = random.sample(list(all_sequences.values()), len(identified_sequences))
    # Write the random sequences to the output file
    with open(output_file, 'a') as f:
        SeqIO.write(random_sequences, f, "fasta")

# If this script is run from the command line
if __name__ == "__main__":
    # Call the main function with the command line arguments
    main(sys.argv[1], sys.argv[2], sys.argv[3])