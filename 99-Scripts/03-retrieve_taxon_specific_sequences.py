#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import urllib.request
from Bio import Entrez

# Set email address to avoid overloading NCBI's servers
Entrez.email = "your_email@example.com"

def download_species_list():
    """
    Download a list with all species and taxonomic lineage contained in GenBank
    """
    url = "ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdmp.zip"
    filename = "taxdmp.zip"
    urllib.request.urlretrieve(url, filename)
    os.system(f"unzip -p {filename} names.dmp | awk -F '\\t\\|\\t' '$5 == \"scientific name\" {{ print $1 \"\\t\" $3 }}' > species.txt")
    os.system("rm -f names.dmp nodes.dmp delnodes.dmp merged.dmp citations.dmp division.dmp gencode.dmp readme.txt")

def get_taxon_id(taxon):
    """
    Get the taxon ID of a given taxon at any taxonomic level
    """
    handle = Entrez.esearch(db="taxonomy", term=taxon)
    record = Entrez.read(handle)
    count = int(record["Count"])
    if count > 0:
        handle = Entrez.esearch(db="taxonomy", term=taxon, retmax=count)
        record = Entrez.read(handle)
        id_list = record["IdList"]
        for tax_id in id_list:
            handle = Entrez.efetch(db="taxonomy", id=tax_id)
            tax_record = Entrez.read(handle)
            lineage = tax_record[0]["Lineage"]
            if taxon in lineage:
                return tax_id
    return None

def search_genomes(taxa, rank):
    """
    Search for genomes in GenBank for a list of taxa at any taxonomic level
    and return a list of taxa at the genus or species level
    """
    taxa_list = []
    for taxon in taxa:
        tax_id = get_taxon_id(taxon)
        if tax_id is not None:
            handle = Entrez.esearch(db="genome", term=f"txid{tax_id}[Organism]", retmax=100000)
            record = Entrez.read(handle)
            count = int(record["Count"])
            if count > 0:
                handle = Entrez.esummary(db="genome", term=f"txid{tax_id}[Organism]", retmax=count)
                summary = Entrez.read(handle)
                for record in summary:
                    lineage = record["Lineage"]
                    if rank == "genus":
                        taxa_list.append(lineage.split(";")[0].split()[-1])
                    else:
                        taxa_list.append(record["Organism"])
    return sorted(set(taxa_list))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for genomes in GenBank")
    parser.add_argument("taxa", metavar="TAXA", type=str, nargs="+",
                        help="a taxon, comma separated list of taxa, or text file with list of taxa")
    parser.add_argument("-r", "--rank", metavar="RANK", type=str, default="genus",
                        choices=["genus", "species"],
                        help="taxonomic rank to return (genus or species, default: genus)")
    parser.add_argument("-o", "--output", metavar="FILE", type=str, default="taxa
