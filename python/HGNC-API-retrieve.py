import requests as r
import json
import csv
import pprint


base_link="https://rest.genenames.org/fetch/symbol/"

hgnc_symbol_input=input()


    #symbol="CHEK1"

headers={'Accept': 'application/json'}
file="json-data.json"

#search=r.get(f"{base_link}/{symbol}", headers=headers)
search=r.get("https://rest.genenames.org/fetch/symbol/ABL1", headers=headers)

data=search.json()
a=json.loads(search._content)
count=a["response"]["numFound"]

if count < 1 :
    print("No occurences of target found in HGNC API")
elif count==1:
    print("Status code:",search.status_code)
    print(data["response"]["docs"][0]["hgnc_id"])
    print(data["response"]["docs"][0]["symbol"])
    print(data["response"]["docs"][0]["name"])
elif count > 2:
     print("Multiple occurences of target found in HGNC API")

