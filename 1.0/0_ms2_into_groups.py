#!/usr/bin/python3

import pandas as pd
import numpy as np
import glob,os,re,sys,shutil,argparse
from natsort import natsorted
from itertools import zip_longest

###############################################
# Functions:

### get begin and end indices into tuples:
def get_indices(file):
    begin_line_indexes = []
    end_line_indexes = []

    with open(file,'r') as ms2_consensus:
        for i, line in enumerate(ms2_consensus.readlines()):
            if 'BEGIN' in line:
            #   extract line index for lines that contain BEGIN
                begin_line_indexes.append(i)

            elif 'END' in line:
                # return index of line after //
                end_line_indexes.append(i+1)

    begin_end_tuple = list(zip(begin_line_indexes, end_line_indexes))

    return begin_end_tuple




#### grouped() groups n features into mgf files
def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


###############################################

### Get arguments from the process call (command line)

parser = argparse.ArgumentParser(description='Separate .mgf file into smaller files')
parser.add_argument('input', help = 'input .mgf file')
args = parser.parse_args()

file = args.input

### Create new dir to have separate mgf files
dirname = 'groups'
if os.path.exists(dirname):
    shutil.rmtree(dirname)
os.makedirs(dirname)

### Get indices of the for making the new groups
begin_end_tuple = get_indices(file)

print(len(begin_end_tuple))

count = 0
for b in begin_end_tuple:
    if b[1]-b[0] < 9:
        begin_end_tuple.pop(count)
        count+=1
    else:
        count+=1

print(len(begin_end_tuple))

lineList = list()
with open(file, 'r') as f:
    lineList = [line.rstrip() for line in f]

### Separate mgf consensus into n files with 5 ms2 spectra
count = 1

for group in list(grouper(begin_end_tuple , 5)):
    with open(dirname+'/group_'+str(count)+'.mgf','w') as out:
        if None in group:
            none_index = group.index(None)
            group = group[:none_index] # easy fix
            for g in group:
                ms2 = lineList[g[0]:g[1]]
                for i in ms2:
                    out.write(i+'\n')
                out.write('\n')
            count+=1
        else:
            for g in group:
                ms2 = lineList[g[0]:g[1]]
                for i in ms2:
                    out.write(i+'\n')
                out.write('\n')
            count+=1

