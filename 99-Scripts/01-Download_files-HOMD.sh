#!/bin/bash
# Run

#workDir=$1
mkdir HOMD_16S_DB

if [ -d "HOMD_16S_DB" ] 
then
    continue
else
    echo "Creating directory: $PWD/HOMD_16S_DB"
    mkdir HOMD_16S_DB
fi

# folder for original files from HOMD
myDate=$( date '+%Y_%m_%d' )
dir_DB=HOMD_16S_DB/${myDate}-HOMD-16S_DB

if [ -d "$dir_DB" ] 
then
    echo "Directory $PWD/$dir_DB exists." 
    exit 9999 # die with error code 9999
else
    mkdir $dir_DB
    wget https://www.homd.org/ftp/16S_rRNA_refseq/HOMD_16S_rRNA_RefSeq/current/seqid_info.txt -P $dir_DB

    myDate=$( date '+%Y_%m_%d' )

    mv $dir_DB/seqid_info.txt $dir_DB/seqid_info-$myDate.txt
    cp $dir_DB/seqid_info-$myDate.txt HOMD_16S_DB/seqid_info-latest.txt

    wget https://www.homd.org/ftp/16S_rRNA_refseq/HOMD_16S_rRNA_RefSeq/current/HOMD_16S_rRNA_RefSeq_V15.22.fasta -P $dir_DB

    myDate=$( date '+%Y_%m_%d' )

    mv $dir_DB/HOMD_16S_rRNA_RefSeq_V15.22.fasta $dir_DB/HOMD_16S_rRNA_RefSeq_V15.22-$myDate.fasta
    cp $dir_DB/HOMD_16S_rRNA_RefSeq_V15.22-$myDate.fasta HOMD_16S_DB/HOMD_16S_rRNA_RefSeq-latest.fasta
fi