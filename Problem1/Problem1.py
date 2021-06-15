#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 09:53:48 2021

@author: hienpham
"""
import os 
import math
import sys
import re
from collections import Counter


file_path = r"/home/hienpham/Bureau/Bioinformatics_contest/Problem1/2.txt"
afile = open(file_path, 'r')

answer_file = open('output.txt', 'w')


def func(string_list, n_bits, l):
    
    combinations = []
    for i in range(l):
        bits = ''
        if n_bits != 1 :
            for j in range(n_bits):
                bits += string_list[j][i]
        else:
            bits += string_list[0][i]
        combinations.append(bits)
    
    counts = Counter(combinations)
    n_class = len(counts)
    
    ith_class = 1
    encode_dict = dict()
    
    for element in counts:
        encode_dict.update({element: ith_class})
        ith_class += 1
    
    states = []
    for com in combinations:
        encode_val = encode_dict[com]
        states.append(encode_val)
        
    return n_class, states

#string_list = ["00001111", "11001010", "10010011"]
#n_bits = 3
#l = 8

#n_class, states = func(string_list, n_bits, l)


while(True):
    n = int(afile.readline())
    
    for i in range(n):
        n_bits, l = [int(i) for i in afile.readline().rstrip("\r\n").split()]
        string_list = []
        for j in range(n_bits):
            #a = afile.readline().rstrip("\r\n")
            string_list.append(afile.readline().rstrip("\r\n"))
            #string_list.append(a)
        n_class, states = func(string_list, n_bits, l)
        answer_file.write(str(n_class) + "\n")
        answer_file.write(" ".join(map(str, states)) + "\n")
        #answer_file.write('\n')
        
    
    answer_file.close()
    break
    
afile.close()
