#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:46:03 2021

@author: hienpham
"""
import os
import math
import sys
import resource
from collections import Counter


resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**9)

file_path = r"/home/hienpham/Bureau/Bioinformatics_contest/Problem2/4.txt"
afile = open(file_path, 'r')

answer_file = open('output2_3.txt', 'w')


def pos_bin_search(val, ele, arr):
    
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
            #high = mid - 1
            if low != 0:
                pos_val = arr[low - 1:high + 1]
            else:
                pos_val = arr[low:high + 1]
                
            sub_arr = [abs(val - ele - x) for x in pos_val]
            min_delta = min(sub_arr)
            delta_ind = sub_arr.index(min_delta)
            return pos_val[delta_ind]
        else:
            return arr[mid]
    return arr[len(arr) - 1]
 
    
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
            #low = mid + 1
            
            neg_val = arr[low:high + 1]
            sub_arr = [abs(val - ele - x) for x in neg_val]
            min_delta = min(sub_arr)
            delta_ind = sub_arr.index(min_delta)
            return neg_val[delta_ind]
        else:
            return arr[mid]
    return arr[0]

"""
def pos_bin_search(val, ele, arr):
    
    med_val = arr[len(arr)//2]
    
    if len(arr) == 1:
        return arr[0]
    
    if val - (med_val + ele) > 0:
        pos_val = arr[len(arr)//2:]
        add = pos_bin_search(val, ele, pos_val)
        return add
    
    else:
        pos_val = arr[:len(arr)//2 + 1]
        sub_arr = [abs(val - ele - x) for x in pos_val]
        min_delta = min(sub_arr)
        delta_ind = sub_arr.index(min_delta)
        return pos_val[delta_ind]
        

def neg_bin_search(val, ele, arr):
    med_val = arr[len(arr)//2]
    
    if len(arr) == 1:
        return arr[0]
    
    if val - (med_val + ele) < 0:
        neg_val = arr[:len(arr)//2 + 1]
        add = neg_bin_search(val, ele, neg_val)
        return add
        
    else:
        neg_val = arr[len(arr)//2:]
        sub_arr = [abs(val - ele - x) for x in neg_val]
        min_delta = min(sub_arr)
        delta_ind = sub_arr.index(min_delta)
        return neg_val[delta_ind]
"""

def func(m, a, s, M, K, N):
    
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
            if val - ele > 0:
                #do binary search for positive values
                add = pos_bin_search(val, ele, arr_pos)
                
            elif val - ele < 0:
                #do binary search for negative values
                add = neg_bin_search(val, ele, arr_neg)
                
            else:
                #search for smallest value
                add = min(a) #fix this!!!
            #print("{} / {}".format(m.index(ele), s.index(val)))    
            nominee_delta = abs(val - (ele + add))
            if nominee_delta < min_delta and ele + add > 0:
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