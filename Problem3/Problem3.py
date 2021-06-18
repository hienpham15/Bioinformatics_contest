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
    def __init__(self, ic, idx):
        self.data = ic
        self.index = idx
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        self.children.append(child)


def createNode(v_id, i, created, ic):
    
    if created[i] is not None:
        return
    
    created[i] = Node(ic, i)
    if created[v_id[i-1] - 1] is None:
        createNode(v_id, v_id[i-1], created, ic)
        
    p = created[v_id[i-1] - 1]
    p.add_child(created[i])


def createTree(ic, v_id):
    Tree = Node(ic[0], 0) # root
    
    created = [None for i in range(len(ic))]
    
    created[0] = Tree
    for i in range(1, len(ic)):
        createNode(v_id, i, created, ic[i])
        
    return Tree 


ic = [5, 7, 8, 13, 18, 14, 15, 21, 20, 29]
v_id = [1, 1, 3, 3, 4, 4, 5, 5, 5]
tree = createTree(ic, v_id)
euler = []
level = []


def euler_walk(tree, current, previous, depth):
    
    visited = []
    level.append(depth)
    euler.append(current)
    
    for child in tree.children:
        #euler.append(child.index)
        if child.index != previous:
            euler_walk(child, child.index, tree.index, depth + 1)
            euler.append(tree.index)
            level.append(depth)
    return 


e_w = euler_walk(tree, tree.index, tree.index, 0)

def func(n_vertices, v_id, ic, m, q_set, nq, p_set):
    
    tree = createTree(ic, v_id)
    
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