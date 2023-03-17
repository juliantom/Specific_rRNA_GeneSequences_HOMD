#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import subprocess
import json
import datetime
import os

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

# Define command line arguments
parser = argparse.ArgumentParser(description='Retrieve genome names from NCBI databases for a given taxon.')
parser.add_argument('--taxon', required=True, help='Taxon name (comma separated list of taxa, or taxon list stored in a file)')
parser.add_argument('--db_source', default='RefSeq', choices=['GenBank', 'RefSeq', 'all'], help='Database source')
parser.add_argument('--prefix', default='out', help='Prefix for output file')
parser.add_argument('--tax_rank', default='genus', choices=['genus', 'species'], help='Taxonomic rank')

# Parse command line arguments
args = parser.parse_args()

# Get basename and path from prefix
my_path = f'{args.prefix}'
prefix_user = os.path.basename(my_path)
prefix_path_user = os.path.dirname(my_path)

# Build the command string
command = f'datasets summary genome taxon "{args.taxon}" --as-json-lines --assembly-source {args.db_source} | dataformat tsv genome --fields organism-name | grep -v "New" | grep -v "Organism Name" | sed -e "s/ sp\. oral taxon / sp\.-oral-taxon-/" > {args.prefix}-{args.db_source}-genome_names-{datetime.date.today().strftime("%Y_%m_%d")}.txt'

# print parameters
print(f"\n{Fore.GREEN}{Style.BRIGHT}Parameters for 'datasets' and 'dataformat'\n-----------------------------------")
print(f"{Fore.YELLOW}{Style.NORMAL}Taxon of interest: {Fore.CYAN}'{args.taxon}'\n{Fore.YELLOW}DB source: {Fore.CYAN}{args.db_source}\n{Fore.YELLOW}Target rank: {Fore.CYAN}{args.tax_rank}\n{Fore.YELLOW}Dir path: {Fore.CYAN}{prefix_path_user}\n{Fore.YELLOW}Prefix: {Fore.CYAN}{prefix_user}\n{Fore.YELLOW}Command requested: {Fore.CYAN}{command}\n")

# Execute the command
print(f"{Fore.GREEN}{Style.BRIGHT}Running script...\n-----------------------------------\n{Fore.YELLOW}{Style.NORMAL}This may take a while if {Fore.CYAN}{Style.BRIGHT}{args.taxon} {Fore.YELLOW}{Style.NORMAL}has many genomes.\n...")
subprocess.run(command, shell=True)

# Check if the output file is not empty
with open(f'{args.prefix}-{args.db_source}-genome_names-{datetime.date.today().strftime("%Y_%m_%d")}.txt', 'r') as f:
    output = f.read()

if output:
    # If output is not empty, print the number of genomes retrieved
    genome_names = [line.strip() for line in output.split('\n') if line]
    genome_names = [line.replace('uncultured ','').replace('Candidatus ','').replace('Candidate ','') for line in genome_names]
    if genome_names:
        print(f"{Fore.GREEN}{Style.NORMAL}Fantastic news! {Fore.YELLOW}{Style.NORMAL}\nA total of {Fore.CYAN}{Style.BRIGHT}{len(genome_names)}{Fore.YELLOW}{Style.NORMAL} genomes were retrieved from '{Fore.CYAN}{Style.NORMAL}{args.db_source}' {Fore.YELLOW}{Style.NORMAL}database.")
        print(f'{Fore.YELLOW}{Style.NORMAL}-Output all {Fore.CYAN}{Style.BRIGHT}{args.taxon} {Fore.YELLOW}{Style.NORMAL}genomes: {Fore.CYAN}{Style.NORMAL}{args.prefix}-{args.db_source}-genome_names-{datetime.date.today().strftime("%Y_%m_%d")}.txt','')
        if args.tax_rank == 'genus':
            genome_names = sorted(list(set([line.split()[0] for line in genome_names])))
            with open(f'{args.prefix}-{args.db_source}-genome_names-{datetime.date.today().strftime("%Y_%m_%d")}-genus.txt', 'w') as f:
                f.write('\n'.join(genome_names)+'\n')
        elif args.tax_rank == 'species':
            genome_names = sorted(list(set([' '.join(line.split()[:2]) for line in genome_names])))
            with open(f'{args.prefix}-{args.db_source}-genome_names-{datetime.date.today().strftime("%Y_%m_%d")}-species.txt', 'w') as f:
                f.write('\n'.join(genome_names)+'\n')
        print(f"{Fore.YELLOW}{Style.NORMAL}Corresponding to {Fore.CYAN}{Style.NORMAL}{len(genome_names)} {Fore.YELLOW}{Style.NORMAL}{args.tax_rank}.")
        print(f'{Fore.YELLOW}{Style.NORMAL}-Output all {Fore.CYAN}{Style.BRIGHT}{args.tax_rank} {Fore.YELLOW}{Style.NORMAL}in {Fore.CYAN}{Style.BRIGHT}{args.taxon}:: {Fore.CYAN}{Style.NORMAL}{args.prefix}-{args.db_source}-genome_names-{datetime.date.today().strftime("%Y_%m_%d")}-{args.tax_rank}.txt','\n')
    else:
        print(Fore.RED + "Terrible news! No genome names were retrieved.\nI (the programer) don't know what happend.\nThis message was put in place in case something's terribly messed up.\nLet me know immediatly and run datasets/dataformat from terminal.\n-----------------------------------")
else:
    # If output is empty, print an error message
    print(Fore.RED + "ERROR!\nSomething went wrong :(\n-Check organism name, retry with ‘Candidatus + TAXON’.\n OR\n-The programers messed up and you should let them know.\n-Try datasets/dataformat directly in your terminal and see if it runs smoothly.")
