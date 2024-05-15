from Bio import SeqIO

def count_sequences(input_file):
    normal_count = 0
    reversed_count = 0

    # Read the input .fasta file
    for record in SeqIO.parse(input_file, 'fasta'):
        # Check if the record is a reversed sequence
        if 'REVERSED' in record.id:
            reversed_count += 1
        else:
            normal_count += 1

    print(f"Number of normal sequences: {normal_count}")
    print(f"Number of reversed sequences: {reversed_count}")

# Call the function with your input file
count_sequences('/home/wout/databases/construction/uniref50.fasta')