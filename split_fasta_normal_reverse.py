from Bio import SeqIO

def split_fasta(input_file, normal_output_file, reversed_output_file):
    normal_records = []
    reversed_records = []

    # Read the input .fasta file
    for record in SeqIO.parse(input_file, 'fasta'):
        # Check if the record is a reversed sequence
        if '_REVERSED' in record.id:
            reversed_records.append(record)
        else:
            normal_records.append(record)

    # Write the normal sequences to the normal output file
    SeqIO.write(normal_records, normal_output_file, 'fasta')

    # Write the reversed sequences to the reversed output file
    SeqIO.write(reversed_records, reversed_output_file, 'fasta')

# Call the function with your input and output files
split_fasta('/home/wout/databases/SIHUMI_DB1UNIPROT.fasta', '/home/wout/databases/SIHUMI_DB1UNIPROT_TARGET.fasta', '/home/wout/databases/SIHUMI_DB1UNIPROT_DECOY.fasta')