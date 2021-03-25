#!/usr/bin/python3

"""
Usage: $ ./automate_sirius.py

Goal: Automate Sirius annotation of ms2 spectra

"""

import glob,os,re,sys,shutil,subprocess

# Get arguments from the command line

parser = argparse.ArgumentParser(description='Separate into groups')
parser.add_argument('-i', '--input', help = 'input file')
args = parser.parse_args()

mgf_file = args.input

# Run script to separate file into groups

print('File to be processed: {}'.format(args.input))
print('Starting separation into groups')
subprocess.call(['./0_ms2_into_groups.py', mgf_file])

print('#######################################################')
print('                Separation step done')
print('#######################################################')

# Running SIRIUS

print('Preparing to run SIRIUS')

outdir = 'SIRIUS_output'
indir = 'groups'

files = glob.glob(indir+'/*.mgf') 

for file in files:
    group = file.split('/')[-1].split('.')[0]
    print('###### Working with {}'.format(group))
    print()
    subprocess.call(['./1_sirius_cli_run.sh', os.path.join(outdir, group), file])

print('#######################################################')
print('                  SIRIUS run done')
print('#######################################################')

# Fix and format table

subprocess.call(['./2_fix_sirius_output.py'])
