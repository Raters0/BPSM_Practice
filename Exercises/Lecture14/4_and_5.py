#!/usr/bin/python3

def find_rep_kmer(seq,ksize=2,rep=1):
    all_kmer = []
    # find all kmer
    for kmer_len in range(2,len(seq)):
        for i in range(0,len(seq)-kmer_len+1):
            all_kmer.append(seq[i:i+kmer_len])
    # check replication
    for kmer in set(all_kmer):
        l_kmer = len(kmer)
        rep_num = all_kmer.count(kmer)
        if rep_num > rep and l_kmer==ksize:
            print('%s: %d'%(kmer.upper(),rep_num))
        

seq = input('please input the sequence: ')
ksize = input('please input the kmer size: ')
thres = input('please input the threshold number: ')
print('Find kmers below:')
find_rep_kmer(seq,int(ksize),int(thres))
