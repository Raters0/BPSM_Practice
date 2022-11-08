#!/usr/bin/python3

s = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
def r_seq(s):
    rs = []
    for i in s:
        if i == 'A':
            r = 'T'
        elif i == 'T':
            r = 'A'
        elif i == 'C':
            r = 'G'
        elif i == 'G':
            r = 'C'
        rs.append(r)
    return ''.join(rs)
print(r_seq(s))
