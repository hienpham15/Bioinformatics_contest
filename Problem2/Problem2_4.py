#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 22:10:56 2021

@author: hienpham
"""
import os
import math
import sys
import resource
from collections import Counter


file_path = r"/home/hienpham/Bureau/Bioinformatics_contest/Problem2/2.txt"
afile = open(file_path, 'r')

answer_file = open('output2_4.txt', 'w')


def pos_bin_search(val, ele, arr):
    """
    Parameters
    ----------
    val : value from s array.
    ele : TYPE
        DESCRIPTION.
    arr : TYPE
        DESCRIPTION.

    Returns
    -------
    function performs binary search on positive values of a (adducts) array.
    

    """
    if len(arr) == 1:
        return arr[0]
    else:
        low = 0
        high = len(arr) - 1
        mid = 0
    
    while low <= high:
        mid = (high + low) // 2
        if val - (arr[mid] + ele) > 0:
            low = mid + 1
        elif val - (arr[mid] + ele) < 0:
            high = mid - 1
        else:
            return arr[mid]
        
    if low >= len(arr) - 1:
        return arr[len(arr) - 1]
    elif high <= 0:
        return arr[0]
    else:
        if abs(val - (arr[high] + ele)) > abs(val - (arr[low] + ele)):
            return arr[low]
        else:
            return arr[high]
 
    
def neg_bin_search(val, ele, arr):
    
    if len(arr) == 1:
        return arr[0]
    else:
        low = 0
        high = len(arr) - 1
        mid = 0
    
    while low <= high:
        mid = (high + low) // 2
        if val - (arr[mid] + ele) < 0:
            high = mid - 1
        elif val - (arr[mid] + ele) > 0:
            low = mid + 1 
        else:
            return arr[mid]
        
    if low >= len(arr) - 1:
        return arr[len(arr) - 1]
    elif high <= 0:
        return arr[0]
    else:
        if abs(val - (arr[high] + ele)) > abs(val - (arr[low] + ele)):
            return arr[low]
        else:
            return arr[high]


def func(m, a, s, M, K, N):
    m = [i*10**6 for i in m]
    a = [i*10**6 for i in a]
    s = [i*10**6 for i in s]
    
    j_ind = []
    k_ind = []
    count = 0
    
    pos_val = [x for x in a if x >= 0]
    arr_pos = sorted(pos_val)
    
    neg_val = [x for x in a if x < 0]
    arr_neg = sorted(neg_val)
    
    for val in s:
        count += 1
        print("{} / {}".format(count, N))
        min_delta = math.inf
        for ele in m:
            if val - ele >= 0:
                #do binary search for positive values
                add = pos_bin_search(val, ele, arr_pos)
                
            elif val - ele < 0:
                #do binary search for negative values
                add = neg_bin_search(val, ele, arr_neg)

                
            #print("{} / {}".format(m.index(ele), s.index(val)))    
            nominee_delta = abs(val - (ele + add))
            if nominee_delta < min_delta and ele + add > 0:
                if nominee_delta == 0:
                    j = m.index(ele)
                    k = a.index(add)
                    break
                else:
                    min_delta = nominee_delta
                    j = m.index(ele)
                    k = a.index(add) 
        
        j_ind.append(j + 1)
        k_ind.append(k + 1)        
    
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