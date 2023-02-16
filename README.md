# Retrieving taxon-specific rRNA gene sequences from HOMD
### Instructions
The recommendation is to clone the repository and use the scripts with minimal modification.
```bash
git clone https://github.com/juliantom/Specific_rRNA_GeneSequences_HOMD.git
```
---
### Scripts
Two scripts (99-Scripts folder)  allow extracting 16S rRNA genes (fasta) using a list of taxa stored in an array. The scripts are written in bash and should be able to run in Linux and Unix based systems including Mac OS.
1. **Script-01** will create a folder and download two files from HOMD.
2. **Script-02** will create a second folder, extract the desired 16S rRNA gene sequences using a list of taxa. Finally, it will save the resulting fasta file(s) into the newly created folder.<br>
<br>
See _Instructions.md_ for detailed explanation. <br>

---
### Necessary data from HOMD and target taxa
Files obtained from HOMD (https://www.homd.org/ftp/16S_rRNA_refseq/HOMD_16S_rRNA_RefSeq/current/) on 02/16/2023 (using script-01):
- seqid_info.txt (09-Feb-2021 20:49)
- HOMD_16S_rRNA_RefSeq_V15.22.fasta (09-Feb-2021 20:49)<br>

Taxa of interest:<br>
1. Lachnospiraceae
2. Leptotrichia
3. Veillonella<br>

