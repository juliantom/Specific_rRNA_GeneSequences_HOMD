# Retrieving taxon-specific rRNA gene sequences from HOMD
### Instructions
The recommendation is to clone the repository and use the scripts with minimal modification.
```bash
git clone https://github.com/juliantom/Specific_rRNA_GeneSequences_HOMD.git
```

### Necessary data from HOMD and target taxa
---
Files obtained from HOMD (https://www.homd.org/ftp/16S_rRNA_refseq/HOMD_16S_rRNA_RefSeq/current/) on 02/16/2023:
- seqid_info.txt (09-Feb-2021 20:49)
- HOMD_16S_rRNA_RefSeq_V15.22.fasta (09-Feb-2021 20:49)<br>

Taxa of interest:<br>
1. Lachnospiraceae
2. Leptotrichia
3. Veillonella<br>
---
### Scripts
Two scripts (99-Scripts folder)  allow extracting 16S rRNA genes (fasta) using list of taxa in arrays. The scripts are written in bash and should be able to run in Linux and Unix based systems including Mac OS.

```bash
# Create repository and link
git init
git add ProjectFolderName
git commit -m "first commit"
git remote add origin https://github.com/YourGithubUsername/RepositoryName.git
git push -u origin master
# pull README.md and LICENSE files to match github repository
git pull -f origin main
# add files inside folder
git init
git add .
git add "Folder name"/"File name"
git commit -m "Folder name"/"File name"
git commit -m "Add run" 99-Scripts/01-Download_files-HOMD.sh
git push -u origin main
# remove files
git rm hello.txt
git commit -m "Deleted the file from the git repository"
git push --set-upstream origin main
```

