#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
import os
import ftplib
import zipfile
from datetime import date, timedelta
from Bio import Entrez

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--email', required=True, help='Email to avoid NCBI saturation')
parser.add_argument('--tax_db', default=os.getcwd(), help='Path to store files (default: current folder)')
parser.add_argument('--latest', action='store_true', help='Download the latest version of taxdmp.zip')
parser.add_argument('--force-overwrite', action='store_true', help='Overwrite file if it already exists')
args = parser.parse_args()

# Set up paths
tax_db_dir = os.path.join(args.tax_db, 'GENBANK_TAX')
repo_dir = os.path.join(tax_db_dir, 'repo')
latest_dir = os.path.join(tax_db_dir, 'latest')

# Check if necessary directories exist and create them if they don't
if not os.path.exists(repo_dir):
    os.makedirs(repo_dir)
if not os.path.exists(latest_dir):
    os.makedirs(latest_dir)

# Check if taxdmp.zip exists in latest directory
if os.path.exists(os.path.join(latest_dir, 'taxdmp.zip')):
    if args.latest:
        os.system('rm -rf {}/*'.format(latest_dir))
    else:
        print('A taxdmp.zip file already exists in GENBANK_TAX/latest/. Use --latest to download the latest version.')
        sys.exit()

# Check if file with current date exists in repo directory
today = date.today().strftime('%Y_%m_%d')
if os.path.exists(os.path.join(repo_dir, 'taxdmp-{}.zip'.format(today))):
    if args.force_overwrite:
        os.remove(os.path.join(repo_dir, 'taxdmp-{}.zip'.format(today)))
    else:
        print('A file with the current date already exists in GENBANK_TAX/repo/. Use --force-overwrite to overwrite it.')
        sys.exit()

# Set up FTP connection and download taxdmp.zip file
Entrez.email = args.email
ftp = ftplib.FTP('ftp.ncbi.nlm.nih.gov')
ftp.login()
ftp.cwd('/pub/taxonomy')
filename = 'taxdmp.zip'
with open(os.path.join(latest_dir, filename), 'wb') as f:
    ftp.retrbinary('RETR {}'.format(filename), f.write)

# Move taxdmp.zip to repo directory and rename with current date
new_filename = 'taxdmp-{}.zip'.format(today)
os.rename(os.path.join(latest_dir, filename), os.path.join(repo_dir, new_filename))

# Copy file from repo directory to latest directory
os.system('cp {} {}'.format(os.path.join(repo_dir, new_filename), os.path.join(latest_dir, 'taxdmp.zip')))

# Unzip file in latest directory
with zipfile.ZipFile(os.path.join(latest_dir, 'taxdmp.zip'), 'r') as zip_ref:
    zip_ref.extractall(latest_dir)

print('taxdmp.zip file downloaded and unzipped successfully.')
