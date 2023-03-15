#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script uses the argparse module to allow the user to specify a folder to store the files.
    If no folder is specified, it will use the default folder HOMD_16S_DB."""

import argparse
import datetime
import os
import urllib.request

# Define command line arguments
parser = argparse.ArgumentParser(description='Download HOMD 16S rRNA dataset files')
parser.add_argument('--folder', type=str, default='HOMD_16S_DB', help='Folder to store files')
parser.add_argument('--seqid_name', type=str, default='seqid_info', help='Name for seqid_info file')
parser.add_argument('--fasta_db_name', type=str, default='HOMD_16S_rRNA_RefSeq_V15.22', help='Name for HOMD 16S rRNA fasta file')
args = parser.parse_args()

# Download files
base_url = "https://www.homd.org/ftp/16S_rRNA_refseq/HOMD_16S_rRNA_RefSeq/current/"
date_string = datetime.date.today().strftime('%Y_%m_%d')
seqid_file = f"{args.folder}/{args.seqid_name}-{date_string}.txt"
fasta_file = f"{args.folder}/{args.fasta_db_name}-{date_string}.fasta"

# Check if folder exists, create if it doesn't
if not os.path.exists(args.folder):
    os.mkdir(args.folder)
    print(f"Creating folder for HOMD 16S rRNA Dataset in: {os.getcwd()}/{args.folder}")
else:
    print(f"HOMD 16S rRNA folder FOUND in: {os.getcwd()}/{args.folder}")
    # Check if files exist
    if os.path.exists(seqid_file) and os.path.exists(fasta_file):
        print("Files were found in place.")
        exit()

urllib.request.urlretrieve(f"{base_url}seqid_info.txt", seqid_file)
print(f"Downloaded {seqid_file}")
urllib.request.urlretrieve(f"{base_url}HOMD_16S_rRNA_RefSeq_V15.22.fasta", fasta_file)
print(f"Downloaded {fasta_file}")
