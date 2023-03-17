#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import subprocess
import json
import datetime
import os
import sys

# Import color codes
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

# Call colors
colorama_init()

# Define command line arguments
parser = argparse.ArgumentParser(description='Retrieve genome names from NCBI databases for a given taxon.')
parser.add_argument('--taxon', required=True, help='[str] Taxon name at any rank. Use quotations if name contains two words. Example: "Escherichia coli" ')
parser.add_argument('--db-source', default='RefSeq', choices=['GenBank', 'RefSeq', 'all'], help='[str] Database source for assemblies. GenBank=GCF, RefSeq=GCA, all="GCF + GCA". (default: RefSeq)')
parser.add_argument('--prefix', default='out', help='[str] Prefix for output file; path should be included. (default: out)')
parser.add_argument('--tax-rank', default='genus', choices=['genus', 'species'], help='[str]Taxonomic rank. (default: genus)')
parser.add_argument('--no-log-file', action="store_true",  required=False, help='Do not create a log file. By default the log file will be stored in PREFIX[TAXON]-DB_SOURCE-DATE-log.txt)')

# Parse command line arguments
args = parser.parse_args()

# Get basename and path from prefix
my_path = f'{args.prefix}'
prefix_user = os.path.basename(my_path)
prefix_path_user = os.path.dirname(my_path)

# Build the command string
command = f'datasets summary genome taxon "{args.taxon}" --as-json-lines --assembly-source {args.db_source} | dataformat tsv genome --fields organism-name | grep -v "New" | grep -v "Organism Name" | sed -e "s/ sp\. oral taxon / sp\.-oral-taxon-/" > {args.prefix}-{args.db_source}-{datetime.date.today().strftime("%Y_%m_%d")}-names.txt'

# print parameters
header_1 = f"{Fore.GREEN}{Style.BRIGHT}Parameters for 'datasets' and 'dataformat'\n-----------------------------------"
conditions_1 = f"{Fore.YELLOW}{Style.NORMAL}Taxon of interest: {Fore.CYAN}'{args.taxon}'\n{Fore.YELLOW}DB source: {Fore.CYAN}{args.db_source}\n{Fore.YELLOW}Target rank: {Fore.CYAN}{args.tax_rank}\n{Fore.YELLOW}Dir path: {Fore.CYAN}{prefix_path_user}\n{Fore.YELLOW}Prefix: {Fore.CYAN}{prefix_user}"
conditions_2 = f'{Fore.YELLOW}{Style.NORMAL}Date: {Fore.CYAN}{datetime.date.today().strftime("%Y/%m/%d")}\n'
print(header_1)
print(conditions_1)
print(conditions_2)

# Execute the command
header_2 = f"{Fore.GREEN}{Style.BRIGHT}Running script...\n-----------------------------------\n{Fore.YELLOW}{Style.NORMAL}This may take a while if {Fore.CYAN}{Style.BRIGHT}{args.taxon} {Fore.YELLOW}{Style.NORMAL}has many genomes..."
my_command = f'{Fore.YELLOW}Command requested: {Fore.CYAN}{command}\n'
print(header_2)
print(my_command)
subprocess.run(command, shell=True)

# Check if the output file is not empty
with open(f'{args.prefix}-{args.db_source}-{datetime.date.today().strftime("%Y_%m_%d")}-names.txt', 'r') as f:
    output = f.read()

header_3 = f"{Fore.GREEN}{Style.BRIGHT}Results\n-----------------------------------"
print(header_3)

if output:
    # If output is not empty, print the number of genomes retrieved
    genome_names = [line.strip() for line in output.split('\n') if line]
    genome_names = [line.replace('uncultured ','').replace('Candidatus ','').replace('Candidate ','') for line in genome_names]
    if genome_names:
        footer_sub_1 = f"{Fore.GREEN}{Style.NORMAL}Fantastic news! {Fore.YELLOW}{Style.NORMAL}\nA total of {Fore.CYAN}{Style.BRIGHT}{len(genome_names)}{Fore.YELLOW}{Style.NORMAL} genomes were retrieved from '{Fore.CYAN}{Style.NORMAL}{args.db_source}' {Fore.YELLOW}{Style.NORMAL}database."
        footer_sub_2 = f'{Fore.YELLOW}{Style.NORMAL}-Output all {Fore.CYAN}{Style.BRIGHT}{args.taxon} {Fore.YELLOW}{Style.NORMAL}genomes: {Fore.CYAN}{Style.NORMAL}{args.prefix}-{args.db_source}-{datetime.date.today().strftime("%Y_%m_%d")}-names.txt'
        print(footer_sub_1)
        print(footer_sub_2)
        if args.tax_rank == 'genus':
            genome_names = sorted(list(set([line.split()[0] for line in genome_names])))
            with open(f'{args.prefix}-{args.db_source}-{datetime.date.today().strftime("%Y_%m_%d")}-names-genus.txt', 'w') as f:
                f.write('\n'.join(genome_names)+'\n')
        elif args.tax_rank == 'species':
            genome_names = sorted(list(set([' '.join(line.split()[:2]) for line in genome_names])))
            with open(f'{args.prefix}-{args.db_source}-{datetime.date.today().strftime("%Y_%m_%d")}-names-species.txt', 'w') as f:
                f.write('\n'.join(genome_names)+'\n')
        footer_sub_3 = f'{Fore.YELLOW}{Style.NORMAL}Corresponding to {Fore.CYAN}{Style.NORMAL}{len(genome_names)} {Fore.YELLOW}{Style.NORMAL}{args.tax_rank}.'
        footer_sub_4 = f'{Fore.YELLOW}{Style.NORMAL}-Output all {Fore.CYAN}{Style.BRIGHT}{args.tax_rank} {Fore.YELLOW}{Style.NORMAL}in {Fore.CYAN}{Style.BRIGHT}{args.taxon}: {Fore.CYAN}{Style.NORMAL}{args.prefix}-{args.db_source}-{datetime.date.today().strftime("%Y_%m_%d")}-names-{args.tax_rank}.txt\n'
        print(footer_sub_3)
        print(footer_sub_4)
        footer = f'{footer_sub_1}\n{footer_sub_2}\n{footer_sub_3}\n{footer_sub_4}{Fore.GREEN}{Style.NORMAL}'
    else:
        footer_error_1 = f"{Fore.RED}{Style.BRIGHT}Terrible news!\n{Fore.RED}{Style.NORMAL}I (the programer) don't know what happend.\nThis message was put in place in case something's terribly messed up.\nLet me know immediatly and run datasets/dataformat from terminal.\n"
        footer = f'{footer_error_1}{Fore.GREEN}{Style.NORMAL}'
        print(footer)
else:
    # If output is empty, print an error message
    footer_error_2 = f'{Fore.RED}{Style.BRIGHT}ERROR!\n{Fore.RED}{Style.NORMAL}Something went wrong :(\n-Check organism name, retry with ‘Candidatus + TAXON’.\n OR\n-The programers messed up and you should let them know.\n-Try datasets/dataformat directly in your terminal and see if it runs smoothly.\n'
    footer = f'{footer_error_2}{Fore.GREEN}{Style.NORMAL}'
    print(footer)

# Print to filename.txt
if not f'{args.no_log_file}' == 'False':
    header_4 = f"{Fore.RED}{Style.BRIGHT}LOG file\n-----------------------------------"
    footer_log = f"{Fore.RED}{Style.NORMAL}No log file for yor search.\nI (the developer) think this is the wrong decision.\nBut, it's your call, you probaly don't even need it anyway."
    print(header_4)
    print(footer_log)
else:
    my_log_file = f'{args.prefix}-{args.db_source}-{datetime.date.today().strftime("%Y_%m_%d")}-{args.tax_rank}-log'
    header_4 = f"{Fore.GREEN}{Style.BRIGHT}LOG file\n-----------------------------------"
    footer_log = f"{Fore.YELLOW}{Style.NORMAL}LOG file can be found: {Fore.CYAN}{my_log_file}.txt\n"
    print(header_4)
    print(footer_log)
    original_stdout = sys.stdout # Save a reference to the original standard output
    with open(f'{my_log_file}.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(header_1)
        print(conditions_1)
        print(conditions_2)
        print(header_2)
        print(my_command)
        print(header_3)
        print(footer)
        print(header_4)
        print(footer_log)
        print('')
        sys.stdout = original_stdout # Reset the standard output to its original value