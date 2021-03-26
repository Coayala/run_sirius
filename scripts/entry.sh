# Get file name from command line

file=$1

# Run separate into groups

python3 0_ms2_into_groups.py ${file}

# Run steps for multiple groups

python3 1_automate_python.py

# Run fix table step

python3 2_fix_sirius_output.py
