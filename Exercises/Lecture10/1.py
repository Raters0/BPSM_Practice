#!/usr/bin/python3

s = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
na = s.count('A')
nt = s.count('T')
r = (na+nt)/len(s)
print('the ratio of A+T is: ',r )


