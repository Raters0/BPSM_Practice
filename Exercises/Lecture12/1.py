#!/usr/bin/python3

with open('input.txt','r') as obj:
    contents = obj.readlines()

clean_seqs = []
for seq in contents:
    clean_seqs.append(seq[14:])

with open('cleaned_seqs.txt','w') as obj:
    for seq in clean_seqs:
        obj.write(seq)
