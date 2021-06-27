#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 21:16:40 2021

@author: hienpham
"""

import os
import math
import sys
import resource
from collections import Counter


file_path = r"/home/hienpham/Bureau/Bioinformatics_contest/Final/Problem1/test1.txt"
afile = open(file_path, 'r')

answer_file = open('output1_4.txt', 'w')


def seq_sum (seq1, seq2):
    seq_s = ''
    for i in range(len(seq1)):
        ans = int(seq1[i]) + int(seq2[i])
        seq_s += str(ans)
    return seq_s


def func(n, m, hap1, hap2, str3):
    q_idx = [i for i in range(len(str3)) if str3[i] == '?']
    not_q_idx = [i for i in range(len(str3)) if str3[i] != '?']
    n_gaps = len(q_idx) - 1
    pairs_dict = {}
    
    hap_merge = hap1 + hap2
    
    for i in range(n_gaps):
        seq = str3[q_idx[i]+1:q_idx[i+1]]
        for j in range(len(hap_merge) - 1):
            hap1_seq = hap_merge[j][q_idx[i]+1:q_idx[i+1]]
            
            for k in range(j + 1, len(hap_merge)):
                hap2_seq = hap_merge[k][q_idx[i]+1:q_idx[i+1]]
                
                if seq_sum(hap1_seq, hap2_seq) == seq:
                    if (j, k) in pairs_dict:
                        pairs_dict[(j ,k)] += 1
                    else:
                        pairs_dict.update({(j, k):1})
    
    dict_max = max(pairs_dict.values())
    pairs = [pair for pair, val in pairs_dict.items() if val == dict_max]
    id1, id2 = pairs[0][0], pairs[0][1]
    
    seq_pair = seq_sum(hap_merge[id1], hap_merge[id2])
      
    for i in (not_q_idx):
        if seq_pair[i] != str3[i]:
            seq_pair = seq_pair[:i] + str3[i] + seq_pair[i+1:] 
        
    return seq_pair

#n, m = 3, 2
#hap1 = ['010011', '101110', '011101']
#hap2 = ['110111', '011101', '001101']
#str3 = '?11?2?'
#ans = func(n, m, hap1, hap2, str3)



while(True):
    n, m = [int(i) for i in afile.readline().rstrip("\r\n").split()]
    
    hap1 = []
    hap2 = []
    gen = []
    
    count = 0
    
    for i in range(n):
        afile.readline()
        str1 = afile.readline().rstrip("\r\n").split()
        str2 = afile.readline().rstrip("\r\n").split()
        
        hap1.append(str1[0])
        hap2.append(str2[0])
    
    for j in range(m):
        afile.readline()
        str3 = afile.readline().rstrip("\r\n").split()
        
        gen.append(str3)
    
        ans = func(n, m, hap1, hap2, str3[0])
        answer_file.write(str(ans) + "\n")
        
        count += 1
        
        print("{} / {}".format(count, m))
               
    answer_file.close()
    break
    
afile.close()