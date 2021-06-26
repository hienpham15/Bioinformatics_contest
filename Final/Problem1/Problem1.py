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


file_path = r"/home/hienpham/Bureau/Bioinformatics_contest/Final/Problem1/1.txt"
afile = open(file_path, 'r')

answer_file = open('output1_4.txt', 'w')



def func(n, m, hap1, hap2, str3):
    
    return ans

#M, K, N = 5, 4, 7
#m = [0.000001, 0.000002, 0.000003, 0.000004, 0.000005]
#a = [0.000002, 0.000010, 0.000001, -0.000001]
#s = [0.000001, 0.000002, 0.000100, 0.000005, 0.000020, 0.000010, 0.000003]
#j_ind, k_ind = func(m, a, s, M, K, N)

hap1 = []
hap2 = []
gen = []

while(True):
    n, m = [int(i) for i in afile.readline().rstrip("\r\n").split()]
    
    for i in range(n):
        afile.readline()
        str1 = afile.readline().rstrip("\r\n").split()
        str2 = afile.readline().rstrip("\r\n").split()
        
        hap1.append(str1)
        hap2.append(str2)
    
    for j in range(m):
        afile.readline()
        str3 = afile.readline().rstrip("\r\n").split()
        
        gen.append(str3)
    
        ans = func(n, m, hap1, hap2, str3)
        answer_file.write(str(ans) + "\n")
               
    answer_file.close()
    break
    
afile.close()