# Retrieving taxon-specific rRNA gene sequences from HOMD
The goal of these programs is to obtain 16S rRNA genes (variable region) from the Human Oral Microbiome Database using genus or species information from NCBI databases (GenBank, RefSeq or both). It uses HOMD 16S rRNA dataset and NCBI *datasets* command-line tool obtained form GitHub.<br>

### Instructions
1. Obtain the repository
```bash
# Create and move to a working directory (example: 'myRibosomalGenes')
mkdir myOralRibosomalGenes && cd myOralRibosomalGenes

# Clone the repository
git clone https://github.com/juliantom/Specific_rRNA_GeneSequences_HOMD.git

# Change to folder 
cd Specific_rRNA_GeneSequences_HOMD

# Make scripts executable and available
chmod +x 99-Scripts/*.py
export PATH="$PWD/bin:$PATH"

```
2. Check if required programs are in the PATH
```bash
# This program will try to find 'datasets' and 'dataformat' programs. See help menu for other uses.
./99-Scripts/01-check_programs.py
```
3. Setup HOMD database (16S rRNA genes - RefSeq). This will download two files from the HOMD website (seqid and fasta file). *This only needs to be done once, HOMD is updated ~6-12 months.*
```bash
99-Scripts/02-download_16S_rRNA_DB_HOMD.py
```
4. For your target taxon, create a list of unique genus or species from genomes deposited in NCBI (GenBank, RefSeq, both).
```bash
# Change to your working dir
cd ..
# Create taxon list
Specific_rRNA_GeneSequences_HOMD/99-Scripts/03-create_taxon_list.py
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

### Citations
* Chen T, Yu WH, Izard J, Baranova OV, Lakshmanan A, Dewhirst FE. The Human Oral Microbiome Database: a web accessible resource for investigating oral microbe taxonomic and genomic information. Database (Oxford). 2010 Jul 6;2010:baq013. doi: 10.1093/database/baq013. PMID: 20624719; PMCID: PMC2911848.
* Escapa IF, Chen T, Huang Y, Gajare P, Dewhirst FE, Lemon KP. New Insights into Human Nostril Microbiome from the Expanded Human Oral Microbiome Database (eHOMD): a Resource for the Microbiome of the Human Aerodigestive Tract. mSystems. 2018 Dec 4;3(6):e00187-18. doi: 10.1128/mSystems.00187-18. PMID: 30534599; PMCID: PMC6280432.
* NCBI *datasets* [https://www.ncbi.nlm.nih.gov/datasets/].

### Databases and program versions
* HOMD 16S rRNA data (v15.22) [https://www.homd.org/ftp/16S_rRNA_refseq/HOMD_16S_rRNA_RefSeq/current/]
    * seqid_info.txt
    * HOMD_16S_rRNA_RefSeq_V15.22.fasta
* NCBI *datasets* (v14.17.0) [https://github.com/ncbi/datasets]
* Programs written with *Python* (v3.9.7)