# Master's dissertation Wout Cattrijsse 2023-2024
## Assessment of database construction and reduction methods in metaproteomics
This GitHub repository contains all the code and analysis work conducted for the Master Dissertation, which was used to compile the master thesis. Within the root directory, you'll find folders, files, and scripts and more detailed information about the contents of each can be found in the README.md files located within the respective folders./
[count_normal_reverse_sequences.py](https://github.com/WoutCatt/lab_notebook_masters_dissertation/blob/main/count_normal_reverse_sequences.py) is a python script that takes a .fasta file as input and counts how many normal and reversed sequences are in the file.
[enriched_database_generation.py](https://github.com/WoutCatt/lab_notebook_masters_dissertation/blob/main/enriched_database_generation.py) is a python script that takes all .xml files (X!Tandem output) from a specified directory, a .fasta file (usually the protein sequence database that was used in the search) and the location of the output file as input and compares the identified proteins to the protein sequences from the .fasta file. All corresponding protein sequences are added to a new .fasta file which is given as output with the specified name at the specified location.
[fasta_sectioning.py](https://github.com/WoutCatt/lab_notebook_masters_dissertation/blob/main/fasta_sectioning.py) is a python script that takes a .fasta file as input and divides the input file into a specified number of sections (n) that are of equal length. (If the amount of sequences is not perfectly divisible by n, the remaining sections are added to the final .fasta file. The output is a directory containing all sections in separate .fasta files. 
[ftp_download.sh](https://github.com/WoutCatt/lab_notebook_masters_dissertation/blob/main/ftp_download.sh) is a shell script that downloads files from ftp links specified by the user.
[generate_reversed_fasta.py](https://github.com/WoutCatt/lab_notebook_masters_dissertation/blob/main/generate_reversed_fasta.py) is a python script that takes a .fasta file and the location of the output file as input and gives a .fasta file where all the protein sequences are reversed as output.
[merge_fastas.py](https://github.com/WoutCatt/lab_notebook_masters_dissertation/blob/main/merge_fastas.py) is a python script that takes two .fasta files and the location of the output file as input and merges these files into a single .fasta file that is given as the output.
[run_sage_nextflow.sh](https://github.com/WoutCatt/lab_notebook_masters_dissertation/blob/main/run_sage_nextflow.sh) is a shell script that uses user defined combinations .json files and .mzml files and runs Sage searches on each of the matching .json and .mzml files. It gives .sage.tsv files as output. The Nextflow pipeline used in the script is written by [Michael Lazear](https://github.com/lazear/sage)
[run_xtandem.sh](https://github.com/WoutCatt/lab_notebook_masters_dissertation/blob/main/run_xtandem.sh) is a shell script that takes an array of .fasta files and an array of .xml files as input and performs an X!Tandem search on every nth .xml file against its corresponding nth .fasta file. It gives .xml files for every search as output.
[run_xtandem_sections](https://github.com/WoutCatt/lab_notebook_masters_dissertation/blob/main/run_xtandem_sections.sh) is a shell script that takes a directory of .fasta files and an array of .xml files as input and performs an X!Tandem search on each of the .fasta files with each of the .xml files. This is used to efficiently perform the database sectioning method searches.
[split_fasta_normal_reverse.py](https://github.com/WoutCatt/lab_notebook_masters_dissertation/blob/main/split_fasta_normal_reverse.py) is a python script that takes a .fasta file and two locations of the two output files as input. It splits the .fasta file into two different .fasta files based on the presence of user-specified tag in the protein_id.
