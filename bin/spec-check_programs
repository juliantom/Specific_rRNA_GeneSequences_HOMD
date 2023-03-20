#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script uses the argparse module to allow the user to specify a folder to store the files.
    If no folder is specified, it will use the default folder HOMD_16S_DB."""

import argparse
import os

# Define command line arguments
parser = argparse.ArgumentParser(description='Check if programs exist in the path')
parser.add_argument('--programs', type=str, default='datasets,dataformat', help='Comma separated list of programs or text file with vertical list of programs (one per line)')
args = parser.parse_args()

# Read program list from text file if provided
if os.path.isfile(args.programs):
    with open(args.programs) as f:
        programs = [line.strip() for line in f]
else:
    programs = args.programs.split(',')

# Check if programs exist
for program in programs:
    if os.system(f"which {program} >/dev/null 2>&1") == 0:
        print(f"{program}: FOUND")
    else:
        print(f"{program}: NOT FOUND")
