#!/usr/bin/python3

import pandas as pd
import numpy as np
import glob,os,re,sys
from natsort import natsorted
import requests
import time
import json
import io
import pprint

s = requests.Session()
main_url = "https://cts.fiehnlab.ucdavis.edu/rest/"


def split(a, n):
    """
    Function to split list a in n groups
    """
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

str_candidates_files = natsorted(glob.glob('sirius/SIRIUS_output/group_*/compound_identifications.tsv'))
print(len(str_candidates_files))
pprint.pprint(str_candidates_files[:2])

canopus_files = natsorted(glob.glob('SIRIUS_output/group_*/canopus_summary.tsv'))
print(len(canopus_files))
pprint.pprint(canopus_files[:2])

summary_df = pd.DataFrame()

for file in str_candidates_files:

    intermediate_df = pd.read_csv(file, sep='\t')

    intermediate_df['Features'] = intermediate_df['id'].str.split('_').str[-1]

    col_list = [
        'Features', 'molecularFormula',
        'adduct', 'InChI', 'smiles', 'links',
    ]
    intermediate_df = intermediate_df.loc[:, col_list]

    summary_df = pd.concat([summary_df, intermediate_df], axis=0)


print(summary_df.shape)

canopus_df = pd.DataFrame()

for file in canopus_files:

    intermediate_df = pd.read_csv(file, sep='\t', index_col=False)

    if not intermediate_df.empty:

        intermediate_df['Features'] = intermediate_df['name'].str.split(
            '_').str[-1]
        intermediate_df = intermediate_df.loc[:, [
            'Features', 'all classifications', 'superclass', 'class',
            'subclass'
        ]]

        canopus_df = pd.concat([canopus_df, intermediate_df],
                            axis=0).reset_index(drop=True)

    else:
        continue

summary_df = summary_df.merge(canopus_df, on="Features", how='left')

print(summary_df.shape)

summary_df.head()

annotation_df = summary_df.copy()

## Extract HMDB, YMDB and KNApSAcK hits
reg_expr = '\(([^)]+)\)'
to_extract = [('HMDB', 'HMDB:'+reg_expr),
              ('YMDB', 'YMDB:'+reg_expr), 
              ('KNApSAcK', 'KNApSAcK:'+reg_expr),
              ('CHEBI', 'CHEBI:'+reg_expr),
              ('PlantCyc', 'Plantcyc:'+reg_expr),
              ('BioCyc', 'Biocyc:'+reg_expr), 
              ('KEGG', 'KEGG:'+reg_expr),
              ('COCONUT', 'COCONUT:'+reg_expr),
              ('PubChem_CID', 'PubChem:'+reg_expr)]

for t in to_extract:
    annotation_df[t[0]] = annotation_df['links'].str.extract(t[1]).fillna('')

## Fix HMDB, YMDB and KNApSAcK entries
to_fix = [('HMDB',  'HMDB{0:0>7}'),
          ('YMDB',  'YMDB{0:0>5}'), 
          ('KNApSAcK', 'C{0:0>8}'),
          ('CHEBI', 'CHEBI:{}')]

for t in to_fix:
    # print(t)
    for index, row in annotation_df.iterrows():

        if row[t[0]] == "":
            continue
        elif " " in row[t[0]]:
            item_list = [t[1].format(x) for x in row[t[0]].split(' ')]
            item_str = ",".join(item_list)
            # print(t[0], index, row[t[0]], item_str)
            annotation_df.loc[index, t[0]] = item_str
        else:
            item_str = t[1].format(row[t[0]])
            # print(t[0], index, row[t[0]], item_str)
            annotation_df.loc[index, t[0]] = item_str


annotation_df.head()

annotation_df.to_csv('summary_output_SIRIUS.csv', index=False)

exploded_df = annotation_df.copy()

exploded_df['PubChem_CID'] = exploded_df['PubChem_CID'].replace("", 'NA')

exploded_df['PubChem_CID'] = exploded_df['PubChem_CID'].str.split()

exploded_df = exploded_df.explode('PubChem_CID')


list_cid = [x for x in exploded_df['PubChem_CID'].values if x != 'NA' ]

query_list = list(split(list_cid, 10))

query_string = [",".join(x) for x in query_list]

properties = 'MolecularFormula,ExactMass,InChIKey'

all_pubchem_hits = pd.DataFrame()

for query in query_string:

    r = s.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/' +
              query + '/property/' + properties + '/CSV').content
    result_df = pd.read_csv(io.StringIO(r.decode('utf-8')))
    all_pubchem_hits = pd.concat([all_pubchem_hits, result_df], axis=0)
    time.sleep(20)
all_pubchem_hits  


pubchem_hits = all_pubchem_hits.copy()

pubchem_hits['CID'] = pubchem_hits['CID'].astype(str)

merged = exploded_df.merge(pubchem_hits, left_on = "PubChem_CID", right_on = "CID", how = "left")

merged['PubChem_CID'] = merged['PubChem_CID'].replace('NA', '')

merged = merged.drop('CID', axis=1)

print(merged.shape)

merged.to_csv('summary_output_SIRIUS_exploded.csv', index=False)

merged.head()



