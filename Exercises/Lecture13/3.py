#!/usr/bin/python3

contents = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']

# test whether the length for sequence is the same
l = []
for seq in contents:
    l.append(len(seq))
seq_len = len(set(l)) 
if seq_len > 1:
    raise Exception('not all the sequence has the same length!')

#

