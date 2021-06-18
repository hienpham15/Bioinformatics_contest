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

class Tree_decomp:
    def __init__(self):
        self.euler = []
        self.level = []
        
    def euler_walk(self, tree, current, previous, depth):
        self.level.append(depth)
        self.euler.append(current + 1)
    
        for child in tree.children:
            #euler.append(child.index)
            if child.index != previous:
                self.euler_walk(child, child.index, tree.index, depth + 1)
                self.euler.append(tree.index + 1)
                self.level.append(depth)
        return 

    def LCA(self, node_a, node_b):
        id_a = self.euler.index(node_a)
        id_b = self.euler.index(node_b)
        
        if id_a <= id_b:
            depth = min(self.level[id_a:id_b + 1])
            ans = [i for i, j  in enumerate(self.level[id_a:id_b + 1]) if j == depth]
            return self.euler[ans[0] + id_a]
        else:
            depth = min(self.level[id_b:id_a])
            ans = [i for i, j  in enumerate(self.level[id_b:id_a + 1]) if j == depth]
            return self.euler[ans[0] + id_b]
    

def func(v_id, ic, m, q_set, patient_ith):
    
    tree = createTree(ic, v_id)
    tree_decomp = Tree_decomp()
    tree_decomp.euler_walk(tree, tree.index, tree.index, 0)
    
    hpo_set = []
    for i in range(m):    
        disease_ith = q_set[i][1:]
        hpo = 0
        for j in range(len(disease_ith)):
            for k in range(len(patient_ith)):
                node_lca = tree_decomp.LCA(disease_ith[j], patient_ith[k])
                hpo += ic[node_lca - 1]
        
        hpo_set.append(hpo)
    
    disease_id = [i for i, j in enumerate(hpo_set) if j == max(hpo_set)]
    return disease_id[0] + 1

"""
ic = [5, 7, 8, 13, 18, 14, 15, 21, 20, 29]
v_id = [1, 1, 3, 3, 4, 4, 5, 5, 5]
m = 2
q_set = [[2, 4, 2], [1, 10]]
nq = 4
p_set = [[3, 5, 9, 8], [1, 6], [2, 7, 10], [1, 10]]

tree = createTree(ic, v_id)
tree_de = Tree_decomp()
tree_de.euler_walk(tree, tree.index, tree.index, 0)
node = tree_de.LCA(4, 9)
p_ith = p_set[3][1:]
di_id = func(v_id, ic, m, q_set, p_ith)
"""



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
        patient_ith = cq[1:]
        disease_id = func(v_id, ic, m, q_set, patient_ith)
        answer_file.write(str(disease_id) + "\n")
    
    answer_file.close()
    break
    
afile.close()