#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 07:15:42 2021

@author: hienpham
"""
import os 
import math
import sys
import numpy as np


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

file_path = r"/home/hienpham/Bureau/Bioinformatics_contest/Example1/input.txt"
file = open(file_path, 'r')

answer_file = open('output.txt', 'w')
while(True):
    n = int(file.readline())
    
    for i in range(n):
        a, b = [int(i) for i in file.readline().rstrip("\r\n").split()] 
        c = a + b
        answer_file.write(str(c))
        answer_file.write('\n')
        print(c)
    
    answer_file.close()
    break
    
file.close()
        
    

