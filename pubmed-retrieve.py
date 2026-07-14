"""
pubmed_search.py

Minimal wrapper around the NCBI E-utilities API for searching PubMed
and fetching abstracts by PMID.

KNOWN BUG (unfixed as of this commit):
    fetch_pubmed_abstract() requests retmode="json" from efetch.fcgi,
    but efetch does not return JSON for the pubmed database - it returns
    XML regardless of retmode. response.json() will therefore raise
    json.JSONDecodeError, or fail silently on the wrong key structure
    if it doesn't. This function needs to be rewritten to parse XML
    (e.g. via xml.etree.ElementTree or Bio.Entrez) before it can be
    trusted. Do not use in production as-is.

No API key, no rate limiting, no HTTP error handling implemented.
NCBI's unauthenticated rate limit is 3 requests/second (unconfirmed, find documentation).
"""

import requests

def search_pubmed(query):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "retmode": "json",
        "term": query
             }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if "esearchresult" in data and "idlist" in data["esearchresult"]:
        return data["esearchresult"]["idlist"]
    else:
        return []

def fetch_pubmed_abstract(pmid):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "retmode": "json",
        "id": pmid
             }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if "PubmedArticle" in data and data["PubmedArticle"]:
        article = data["PubmedArticle"]
        abstract = article["MedlineCitation"]["Article"]["Abstract"]["AbstractText"]
        return abstract
    else:
        return None

# example:
query = "cancer therapy"
pmids = search_pubmed(query)
for pmid in pmids[:5]:  # get abstracts for the first 5 results
    abstract = fetch_pubmed_abstract(pmid)
    if abstract:
        print(f"PMID: {pmid}")
        print("Abstract:", abstract)
