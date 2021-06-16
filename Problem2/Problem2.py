#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 20:10:14 2021

@author: hienpham
"""
import os
import numpy as np
from collections import Counter


file_path = r"/home/hienpham/Bureau/Bioinformatics_contest/Problem2/2.txt"
afile = open(file_path, 'r')

answer_file = open('output.txt', 'w')


def func(m, a, s, M, K, N):
    
    possible_sums = []
    for i in range(M):
        for j in range(K):
            if m[i] + a[j] > 0:
                possible_sums.append(m[i] + a[j])
            else:
                possible_sums.append(np.inf)
    j_ind = []
    k_ind = []
    for element in s:
        sub_s = [abs(x - element) for x in possible_sums]
        min_delta = min(sub_s)
        delta_ind = sub_s.index(min_delta)
        
        j_ind.append(delta_ind//K + 1)
        k_ind.append(delta_ind%K + 1)
        
        #print("{}/{}".format(len(j_ind), N))
    
    return j_ind, k_ind


#M, K, N = 5, 4, 7
#m = [0.000001, 0.000002, 0.000003, 0.000004, 0.000005]
#a = [0.000002, 0.000010, 0.000001, -0.000001]
#s = [0.000001, 0.000002, 0.000100, 0.000005, 0.000020, 0.000010, 0.000003]
#j_ind, k_ind = func(m, a, s, M, K, N)

while(True):
    n = int(afile.readline())
    
    for i in range(n):
        M, K, N = [int(i) for i in afile.readline().rstrip("\r\n").split()]
        m = [float(i) for i in afile.readline().rstrip("\r\n").split()]
        a = [float(i) for i in afile.readline().rstrip("\r\n").split()]
        s = [float(i) for i in afile.readline().rstrip("\r\n").split()]
        
        j_ind, k_ind = func(m, a, s, M, K, N)
        for k in range(N):
            answer_file.write(str(j_ind[k]) + " " + str(k_ind[k]) + "\n")
               
    
    answer_file.close()
    break
    
afile.close()