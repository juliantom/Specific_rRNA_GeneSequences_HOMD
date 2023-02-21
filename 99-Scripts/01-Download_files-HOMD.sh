#!/bin/bash
# Run

#workDir=$1
myDate=$( date '+%Y_%m_%d' )
workDir=${myDate}-16S_rRNA-HOMD

# folder for original files from HOMD
dirOriginal=$workDir/01-Original_data

mkdir $dirOriginal
wget https://www.homd.org/ftp/16S_rRNA_refseq/HOMD_16S_rRNA_RefSeq/current/seqid_info.txt -P $dirOriginal

myDate=$( date '+%Y_%m_%d' )

mv $dirOriginal/seqid_info.txt $dirOriginal/seqid_info-$myDate.txt

wget https://www.homd.org/ftp/16S_rRNA_refseq/HOMD_16S_rRNA_RefSeq/current/HOMD_16S_rRNA_RefSeq_V15.22.fasta -P $dirOriginal

myDate=$( date '+%Y_%m_%d' )

mv $dirOriginal/HOMD_16S_rRNA_RefSeq_V15.22.fasta $dirOriginal/HOMD_16S_rRNA_RefSeq_V15.22-$myDate.fasta