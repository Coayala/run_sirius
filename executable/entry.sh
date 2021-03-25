# Get file name from command line

file=$1

# Run separate into groups

./0_ms2_into_groups.py ${file}

# Run steps for multiple groups

./1_automate_python.py

# Run fix table step

./2_fix_sirius_output.py
