#!/usr/bin/python3

def check_high_prop(seq,thres):
    # thres should be within [0,1]
    undeter_base = []
    for b in seq:
        if b.upper() not in list('ATCG'):
            undeter_base.append(b)
    undeter_prop = len(undeter_base)/len(seq)
    if undeter_prop >= thres:
        print('WARNING: detecting a high proportion of undeterminded bases: %.2f%%'%(undeter_prop*100))
    else:
        print('It\'s all good!')
