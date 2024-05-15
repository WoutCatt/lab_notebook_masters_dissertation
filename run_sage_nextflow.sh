#!/bin/bash

# List of config files and mzML files
config_files=(
"/home/wout/sage/S11_standard_search_S11_1.json"
"/home/wout/sage/S11_standard_search_S11_2.json"
"/home/wout/sage/S11_standard_search_S11_3.json"
"/home/wout/sage/S11_standard_search_S11_4.json"
# Add more config file paths as needed
)

mzml_files=(
"/home/wout/ms_data/S11_Fraction1.mzML"
"/home/wout/ms_data/S11_Fraction2.mzML"
"/home/wout/ms_data/S11_Fraction3.mzML"
"/home/wout/ms_data/S11_Fraction4.mzML"
# Add more mzML file paths as needed
)

# Check that there are the same number of config and mzML files
if [ ${#config_files[@]} -ne ${#mzml_files[@]} ]; then
  echo "Error: There must be the same number of config files and mzML files."
  exit 1
fi

# Loop over files
for i in "${!config_files[@]}"; do
  config_file="${config_files[$i]}"
  mzml_file="${mzml_files[$i]}"

  echo "Processing config file $config_file and mzML file $mzml_file"

  # Create a copy of script.nf
  cp /home/wout/sage/automatic_annotation/script.nf /home/wout/sage/automatic_annotation/script_${i}.nf

  # Modify the copy to use the correct files
  sed -i "s|params.sage_config_files_location = \".*\"|params.sage_config_files_location = \"$config_file\"|g" /home/wout/sage/automatic_annotation/script_${i}.nf
  sed -i "s|params.mzml_files_location = \".*\"|params.mzml_files_location = \"$mzml_file\"|g" /home/wout/sage/automatic_annotation/script_${i}.nf

  # Run the copy
  /home/wout/sage/nextflow run /home/wout/sage/automatic_annotation/script_${i}.nf
done
