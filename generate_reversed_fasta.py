from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def reverse_sequences(input_file, output_file):
    reversed_records = []

    # Read the input .fasta file
    for record in SeqIO.parse(input_file, 'fasta'):
        # Reverse the sequence
        reversed_seq = Seq(str(record.seq)[::-1])
        
        # Add the _REVERSED tag to the identifier
        reversed_id = record.id + "_REVERSED"
        
        # Create a new SeqRecord for the reversed sequence
        reversed_record = SeqRecord(reversed_seq, id=reversed_id, description="")
        
        reversed_records.append(reversed_record)

    # Write the reversed sequences to the output file
    SeqIO.write(reversed_records, output_file, 'fasta')

# Call the function with your input and output files
reverse_sequences('/home/wout/databases/CAMPI/SIHUMI_S06_10_sections_2.fasta', '/home/wout/databases/CAMPI/SIHUMI_S06_10_sections_REVERSED_2.fasta')