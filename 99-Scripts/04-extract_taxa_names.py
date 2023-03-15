#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

def extract_taxa(taxon, names_file, nodes_file, tax_rank, output_file):
    # Load taxon IDs and ranks from nodes file
    nodes = {}
    with open(nodes_file, "r") as f:
        for line in f:
            fields = line.strip().split("\t|\t")
            tax_id = int(fields[0])
            parent_tax_id = int(fields[1])
            rank = fields[2]
            nodes[tax_id] = {"parent_tax_id": parent_tax_id, "rank": rank}

    # Load taxon names from names file
    names = {}
    with open(names_file, "r") as f:
        for line in f:
            fields = line.strip().split("\t|\t")
            tax_id = int(fields[0])
            name = fields[1]
            name_class = fields[3]
            if name_class in ["scientific name", "synonym"]:
                names[tax_id] = name

    # Find taxon ID for the given taxon name
    tax_id = None
    for tid, name in names.items():
        if name == taxon:
            tax_id = tid
            break
    if tax_id is None:
        raise ValueError(f"Taxon '{taxon}' not found in the taxonomy database")

    # Extract taxa at the specified rank
    taxa = []
    while tax_id != 1:
        if nodes[tax_id]["rank"] == tax_rank:
            taxa.append(names[tax_id])
        tax_id = nodes[tax_id]["parent_tax_id"]
    taxa.reverse()

    # Write taxa to output file
    with open(output_file, "w") as f:
        for taxon in taxa:
            f.write(taxon + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract taxa at a specific rank from the GenBank taxonomy database")
    parser.add_argument("--taxon", type=str, required=True, help="Taxon name to extract")
    parser.add_argument("--names", type=str, required=True, help="Path to names.dmp file")
    parser.add_argument("--nodes", type=str, required=True, help="Path to nodes.dmp file")
    parser.add_argument("--tax_rank", type=str, required=True, choices=["genus", "species"], help="Taxonomic rank to extract")
    parser.add_argument("--output", type=str, required=True, help="Output file")
    args = parser.parse_args()

    extract_taxa(args.taxon, args.names, args.nodes, args.tax_rank, args.output)

