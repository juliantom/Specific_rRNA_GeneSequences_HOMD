# Retrieving specific rRNA gene-sequences from HOMD
## Taxon specific rRNA gene sequences
### This project contains 16S rRNA gene sequences for specific human oral taxa obtained from HOMD.
---
Data obtained from HOMD on 02/16/2023:
1. seqid_info.txt (09-Feb-2021 20:49)
2. HOMD_16S_rRNA_RefSeq_V15.22.fasta (09-Feb-2021 20:49)<br>

Taxa of interest:<br>
1. Lachnospiraceae
2. Leptotrichia
3. Veillonella<br>
---
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

