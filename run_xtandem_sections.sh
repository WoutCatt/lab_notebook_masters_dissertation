#!/bin/bash

# Path to the tandem.exe file
tandem="/home/wout/xtandem/tandem-linux-17-02-01-4/bin/tandem.exe"

# Directory of fasta files
fasta_dir="/home/wout/xtandem/sectioning/SIHUMI_DB1_UNIPROT_10_2"

# Array of input files
files=(
    "/home/wout/xtandem/tandem-win-17-02-01-4/bin/input_S06.xml"
)

# Loop over the XML files
for xml_file in "${files[@]}"; do
    # Get the base name of the XML file (without the directory part)
    xml_base_name=$(basename "$xml_file")

    # Loop over the FASTA files
    for fasta_file in "$fasta_dir"/*.fasta; do
        # Get the base name of the FASTA file
        fasta_base_name=$(basename "$fasta_file")

        # Create the output file name
        output_file="/home/wout/xtandem/output/sectioning/S06/SIHUMI_DB1_10_2/${xml_base_name}_${fasta_base_name}_output.xml"
        
        # Print the paths of the XML and FASTA files
        echo "XML file: $xml_file"
        echo "FASTA file: $fasta_file"
        
        # Modify the taxonomy file
        sed -i "s|URL=\".*\"|URL=\"$fasta_file\"|" /home/wout/xtandem/params/taxonomy_sections.xml

        # Modify the XML file
        sed -i "s|<note type=\"input\" label=\"output, path\">.*</note>|<note type=\"input\" label=\"output, path\">$output_file</note>|" "$xml_file"

        # Print the X!Tandem command
        echo "Running: $tandem \"$xml_file\"" #> \"$output_file.log\" 2>&1"

        # Run X!Tandem and capture its output if needed
        $tandem "$xml_file" #> "$output_file.log" 2>&1
    done
done