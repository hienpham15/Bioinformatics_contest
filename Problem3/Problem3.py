#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 04:53:04 2021

@author: hienpham
"""
import os
import numpy as np
from collections import Counter


file_path = r"/home/hienpham/Bureau/Bioinformatics_contest/Problem3/test1"
afile = open(file_path, 'r')

answer_file = open('output3_1.txt', 'w')


class Node:
    def __init__(self, ic):
        self.data = ic
        self.children = []
        self.parent = None
        
    def add_child(self, child, parent):
        self.children.append(child)


def createNode(v_id, i, created, ic):
    
    if created[i] is not None:
        return
    
    created[i] = Node(ic)
    if created[v_id[i-1]] is None:
        createNode(v_id, v_id[i-1], created, ic)
        
    p = created[v_id[i-1]]
    p.add_child(created[i])


def creatTree(ic, v_id):
    Tree = Node(ic[0]) # root
    
    created = [None for i in range(len(ic))]
    
    created[0] = Tree
    for i in range(1, len(ic)):
        createNode(v_id, i, created, ic[i])
        
    return Tree 



def func(n_vertices, v_id, ic, m, q_set, nq, p_set):
        
    return 






while(True):
    n_vertices = int(afile.readline())
    v_id = [int(i) for i in afile.readline().rstrip("\r\n").split()]
    ic = [int(i) for i in afile.readline().rstrip("\r\n").split()]
    
    m = int(afile.readline())
    q_set = []
    for i in range(m):
        cm = [int(i) for i in afile.readline().rstrip("\r\n").split()]
        q_set.append(cm)
    
    nq = int(afile.readline())
    p_set = []
    for i in range(nq):
        cq = [float(i) for i in afile.readline().rstrip("\r\n").split()]
        p_set.append(cq)
        
    disease_id = func(n_vertices, v_id, ic, m, q_set, nq, p_set)
               
    
    answer_file.close()
    break
    
afile.close()