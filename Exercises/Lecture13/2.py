#!/usr/bin/python3

# set parameter
dna="ATGCATCATG"
k=2 # k-mer
offset=1 # offset for sliding window
n=2 # more than this number found

# create a list for sequences after spliting
contents = []
start = 0
end = start+k
while True:
    contents.append(dna[start:end])
    start += offset
    end = start+k
    if end > len(dna)-1:
        contents.append(dna[start:end])
        break

# count numbers
for seq in set(contents):
    num = contents.count(seq)
    if num > n:
        print('there are '+str(num)+' counts of '+seq)
        
