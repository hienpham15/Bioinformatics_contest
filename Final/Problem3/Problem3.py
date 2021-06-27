#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 13:34:56 2021

@author: hienpham
"""


import os
import math
import sys
import resource
from collections import Counter


file_path = r"/home/hienpham/Bureau/Bioinformatics_contest/Final/Problem3/test1.txt"
afile = open(file_path, 'r')

answer_file = open('output1_1.txt', 'w')


class Node:
    def __init__(self, p_id, p, day):
        self.index = p_id
        self.p = p
        self.day = day
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
        
        

def func(n, m, hap1, hap2, str3):
  
    return seq_pair

#n, m = 3, 2
#hap1 = ['010011', '101110', '011101']
#hap2 = ['110111', '011101', '001101']
#str3 = '?11?2?'
#ans = func(n, m, hap1, hap2, str3)



while(True):
    T = int(afile.readline())
    for i in range(T):
        n_p, n_d = [int(i) for i in afile.readline().rstrip("\r\n").split()]
        
        for j in range(n_d):
            n_contacts = int(afile.readline())
            if n_contacts != 0:
                for k in range(n_contacts):
                    
            
            
    
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