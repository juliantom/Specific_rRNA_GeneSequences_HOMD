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

```bash
The script uses the os.system function to run the which command, which returns the path of the program if it is found in the path or nothing if it is not found. The >/dev/null 2>&1 part of the command redirects all output to the null device so that nothing is printed to the console.

The script first checks if the --programs argument is a file, and if so reads the program list from the file. Otherwise, it splits the argument string on commas to get a list of programs.

For each program in the list, the script checks if it exists in the path and prints either "program name: FOUND" or "program name: NOT FOUND" depending on the result.
```

```bash
This script uses the argparse module to allow the user to specify a folder to store the files. If no folder is specified, it will use the default folder HOMD_16S_DB.

If the specified folder doesn't exist, the script creates it and prints a message to confirm the creation. If the folder already exists, the script checks if the required files already exist in the folder. If the files are found, it prints a message indicating that the files were found and exits. If the files are not found, the script downloads the files from the HOMD website using urllib.request.urlretrieve() and saves them with the current date appended to their filenames.

After downloading the files, the script prints a message indicating which files were downloaded.

````
