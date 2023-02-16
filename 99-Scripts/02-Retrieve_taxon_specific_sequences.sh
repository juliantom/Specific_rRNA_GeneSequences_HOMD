#!/bin/bash
# Run

#workDir=$1
workDir=2023-Tongue_16S_rRNA
# folder for original files from HOMD
dirOriginal=$workDir/01-Original_data
fileSeqID=$dirOriginal/HOMD_16S_rRNA_RefSeq_V15.22-2023_02_16.fasta
dirTaxaFasta=$workDir/02-Taxa_fasta

mkdir $dirTaxaFasta

taxonName=Lachnospiraceae
myTaxonArray=("Butyrivibrio" "Catonella" "Johnsonella" "Lachnoanaerobaculum" "Lachnospir" "Oribacterium" "Shuttleworthia" "Stomatobaculum" "naviforme")

for spGroup in ${myTaxonArray[@]}; do
  grep -A1 "$spGroup" $fileSeqID | grep -v '^-' >>! $dirTaxaFasta/${taxonName}-HOMD_16S_rRNA.fa
done

taxonName=Leptotrichia
myTaxonArray=("Leptotrichia")

for spGroup in ${myTaxonArray[@]}; do
  grep -A1 "$spGroup" $fileSeqID | grep -v '^-' >>! $dirTaxaFasta/${taxonName}-HOMD_16S_rRNA.fa
done

taxonName=Veillonella
myTaxonArray=("Veillonella")

for spGroup in ${myTaxonArray[@]}; do
  grep -A1 "$spGroup" $fileSeqID | grep -v '^-' >>! $dirTaxaFasta/${taxonName}-HOMD_16S_rRNA.fa
done