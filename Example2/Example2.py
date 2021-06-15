#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 08:31:18 2021

@author: hienpham
"""

import os 
import math
import sys
import re


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

file_path = r"/home/hienpham/Bureau/Bioinformatics_contest/Example2/input.txt"
file = open(file_path, 'r')

answer_file = open('output.txt', 'w')


def func(string, sub_string):
    positions = [i.start() + 1 for i in re.finditer('(?=' + sub_string + ')', string)]
    return positions


while(True):
    n = int(file.readline())
    
    for i in range(n):
        string = file.readline().rstrip("\r\n")
        sub_string = file.readline().rstrip("\r\n")
        pos = func(string, sub_string)
        answer_file.write(" ".join(map(str, pos)) + "\n")
        #answer_file.write('\n')
        
    
    answer_file.close()
    break
    
file.close()
        