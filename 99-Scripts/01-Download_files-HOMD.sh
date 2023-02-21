#!/bin/bash
# Run

#workDir=$1
mkdir HOMD_16S_DB
# folder for original files from HOMD
myDate=$( date '+%Y_%m_%d' )
dir_DB=HOMD_16S_DB/${myDate}-HOMD-16S_DB

mkdir $dir_DB
wget https://www.homd.org/ftp/16S_rRNA_refseq/HOMD_16S_rRNA_RefSeq/current/seqid_info.txt -P $dir_DB

myDate=$( date '+%Y_%m_%d' )

mv $dir_DB/seqid_info.txt $dir_DB/seqid_info-$myDate.txt

wget https://www.homd.org/ftp/16S_rRNA_refseq/HOMD_16S_rRNA_RefSeq/current/HOMD_16S_rRNA_RefSeq_V15.22.fasta -P $dir_DB

myDate=$( date '+%Y_%m_%d' )

mv $dir_DB/HOMD_16S_rRNA_RefSeq_V15.22.fasta $dir_DB/HOMD_16S_rRNA_RefSeq_V15.22-$myDate.fasta