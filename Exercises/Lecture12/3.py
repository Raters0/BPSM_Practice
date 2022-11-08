#!/usr/bin/python3

with open('AJ223353_noheader.fasta') as obj:
    seqs = obj.readlines()

new_seqs = []
for s in seqs:
    s=s.strip()
    new_seqs.append(s)

seq = ''.join(new_seqs)

s = 0
e = 30
segments = []
while True:
    if e > len(seq):
        segments.append(seq[s:])
        break
    segments.append(seq[s:e])
    s+=3
    e+=3


# b
n=0
for seg in segments:
    n+=1
    num_g = seg.count('G')
    num_c = seg.count('C')
    ratio = (num_g+num_c)/len(seg)
    print('sequence%d: %s ; GC%%: %.2f'%(n,seg,ratio))


