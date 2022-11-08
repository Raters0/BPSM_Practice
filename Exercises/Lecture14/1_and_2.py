#!/usr/bin/python3

def count_perc(string,target):
    return string.upper().count(target.upper())/len(string)*100


def count_perc_2(string,target_list=list('AILMFWYV')):
    num_list = []
    for a in target_list:
        num_list.append(string.upper().count(a.upper()))
    return sum(num_list)/len(string)*100
