## CHEMBL API - type retrieval from ID
import requests
import json
import csv
import tkinter

#requests.get(url, params={key: value}, args)
id = input('Input the number part of Chembl ID, e.g. 10 for CHEMBL10: ')
r = requests.get('https://www.ebi.ac.uk/chembl/api/data/chembl_id_lookup/CHEMBL'+id+'.json')
print(r.status_code)
print('###')
#print(r.json())
print(r.json()['entity_type'])

#data = r.json()

## ASSAY API 
## https://www.ebi.ac.uk/chembl/api/data/assay/CHEMBL1002069.json

## COMPOUND API 
## https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL10.json

## TARGET API 
## https://www.ebi.ac.uk/chembl/api/data/target/CHEMBL1075138.json
