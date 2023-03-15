# Retrieving taxon-specific rRNA gene sequences from HOMD
The goal of these scripts is to obtain 16S rRNA genes (variable region) from the Human Oral Microbiome Database.<br>
### Instructions
The recommendation is to clone the repository and use the scripts with minimal modification.
```bash
# Create and move to a desired folder (example: 'myRibosomalGenes')
mkdir myOralRibosomalGenes && cd myOralRibosomalGenes

# Clone the repository
git clone https://github.com/juliantom/Specific_rRNA_GeneSequences_HOMD.git

# Change to folder 
cd Specific_rRNA_GeneSequences_HOMD

# Make scripts executable
chmod +x 99-Scripts/*.py

# OPTIONAL
# You can check you have all necessary programs available in the PATH by running the script below
./99-Scripts/01-check_programs.py

# Setup HOMD database (16S rRNA genes - RefSeq). This will download two files from the HOMD website (seqid and fasta file).
# This only needs to be done once, HOMD is updated ~6-12 months.
02-download_16S_rRNA_DB_HOMD.py

# Download database 
./99-Scripts/02-Retrieve_taxon_specific_sequences.py

# 

```
---
### Scripts
Two scripts (99-Scripts folder) allow extracting 16S rRNA genes (fasta) using a list of taxa stored in an array. The scripts are written in bash and should be able to run in Linux and Unix based systems including Mac OS.
1. Assumptions: by default the script will store the corresponding results in a folder under the directory used to store the respository ('myRibosomalGenes'). The output folder name is ()
2. **Script-01** will create a folder and download two files from HOMD.
3. **Script-02** will create a second folder, extract the desired 16S rRNA gene sequences using a list of taxa. Finally, it will save the resulting fasta file(s) into the newly created folder.<br>
- See Instructions.md for detailed explanation.<br>
---
### Necessary data from HOMD and target taxa
Files obtained from HOMD (https://www.homd.org/ftp/16S_rRNA_refseq/HOMD_16S_rRNA_RefSeq/current/) on 02/16/2023 (using script-01):
- seqid_info.txt (09-Feb-2021 20:49)
- HOMD_16S_rRNA_RefSeq_V15.22.fasta (09-Feb-2021 20:49)<br>

Note that the version of the file containing the fasta sequences might be updated.

Test taxa:<br>
1. Lachnospiraceae
2. Leptotrichia
3. Veillonella<br>

