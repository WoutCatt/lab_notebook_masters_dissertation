from Bio import SeqIO

def merge_fasta_files(input_file1, input_file2, output_file):
    records = []

    # Read the first input .fasta file
    for record in SeqIO.parse(input_file1, 'fasta'):
        records.append(record)

    # Read the second input .fasta file
    for record in SeqIO.parse(input_file2, 'fasta'):
        records.append(record)

    # Write the records to the output file
    SeqIO.write(records, output_file, 'fasta')

# Call the function with your input and output files
merge_fasta_files('/home/wout/databases/CAMPI/SIHUMI_S06_10_sections_2.fasta', '/home/wout/databases/CAMPI/SIHUMI_S06_10_sections_REVERSED_2.fasta', '/home/wout/databases/CAMPI/SIHUMI_S06_10_sections_TDA_2.fasta')