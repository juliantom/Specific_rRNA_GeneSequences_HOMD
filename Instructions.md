# Workflow
### This file discribes the steps and scripts followed to obtain 16S rRNA gene sequences from the Human Oral Microbiome Database.
1. Create main (working) folder and download necessary files
```bash
workPath=/Users/julian/Desktop/Active_projects/
workDir=2023-Tongue_16S_rRNA

# Move to folder that will contain the working directory
cd $workPath
# Clone reposirory to obatin scripts
git clone https://github.com/juliantom/Specific_rRNA_GeneSequences_HOMD.git
# Create working folder and move into it
mkdir $workDir
cd $workDir
```
