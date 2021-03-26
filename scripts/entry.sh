# Get file name from command line

file=$1

echo "Starting with file: ${file}"

# Run separate into groups

python3 0_ms2_into_groups.py ${file} > separation.log

echo "##############################################################################"
echo "############     Step 1. Separation into groups has completed     ############"
echo "##############################################################################"

# Run steps for multiple groups

python3 1_automate_sirius.py > sirius_prediction.log

echo "##############################################################################"
echo "############       Step 2. SIRIUS predictions has completed       ############"
echo "##############################################################################"

# Run fix table step

python3 2_fix_sirius_output.py > fix_outputs.log

echo "##############################################################################"
echo "############      Step 3. Fixing output table has completed       ############"
echo "##############################################################################"
