#!/usr/bin/python3

import subprocess

# copy local DNA sequence to working directory
wd = subprocess.getoutput('pwd')
cp_command = 'cp /localdisk/data/BPSM/Lecture11/plain_genomic_seq.txt ' + wd
cp_file = subprocess.run(cp_command,shell=True)

# get local DNA sequence's exons 
with open(wd+'/plain_genomic_seq.txt','r') as obj:
    contents = obj.read()

exon_1 = contents[0:63]
exon_2 = contents[90:]

# get remote sequence
wget_command = 'wget -O ' + wd + '/AJ223353.fasta "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=AJ223353&strand=1&rettype=fasta&retmode=text"'
wget_file = subprocess.run(wget_command, shell=True)

