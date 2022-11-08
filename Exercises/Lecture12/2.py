#!/usr/bin/python3

with open('genomic_dna2.txt') as obj:
    contents1 = obj.read()

with open('exons.txt') as obj:
    contents2 = obj.readlines()

exons = []
for r in contents2:
    num = r.split(',')
    s = int(num[0])
    e = int(num[-1])
    exons.append(contents1[s-1:e])

exon = ''.join(exons)

with open('extracted_exon.txt','w') as obj:
    obj.write(exon)


