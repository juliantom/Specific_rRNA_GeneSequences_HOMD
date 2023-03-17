#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def get_genus_list(taxon):
    url = f"https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={taxon}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    genus_list = []
    for link in soup.find_all("a"):
        if link.get("href") and "genus" in link.get("href"):
            genus_list.append(link.get_text())

    return genus_list

taxon = input("Enter a taxon name (e.g. bacteria, fungi, homo sapiens): ")
genus_list = get_genus_list(taxon)
print(f"Genera within {taxon}: {', '.join(genus_list)}")
