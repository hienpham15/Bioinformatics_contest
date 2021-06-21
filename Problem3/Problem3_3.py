#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 18:13:45 2021

@author: hienpham
"""

import sys
import resource



resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**9)


file_path = r"/home/hienpham/Bureau/Bioinformatics_contest/Problem3/test3"
afile = open(file_path, 'r')

answer_file = open('output3_3.txt', 'w')


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
            #ans = [i for i, j  in enumerate(self.level[id_a:id_b + 1]) if j == depth]
            idx = self.level[id_a:id_b + 1].index(depth)
            return self.euler[idx + id_a]
        else:
            depth = min(self.level[id_b:id_a + 1])
            #ans = [i for i, j  in enumerate(self.level[id_b:id_a + 1]) if j == depth]
            idx = self.level[id_b:id_a + 1].index(depth)
            return self.euler[idx + id_b]


def func(ic, m, q_set, patient_ith, tree_decomp, lut, disease_lut):
       
    hpo_set = []
    
    
    for i in range(m):    
        disease_ith = q_set[i][1:]
        """
        hpo = 0
        for j in range(len(disease_ith)):
            for k in range(len(patient_ith)):
                node_lca = tree_decomp.LCA(disease_ith[j], patient_ith[k])
                hpo = ic[node_lca - 1]
        """
        hpo = 0
        
        for p_pheno in patient_ith:
            ic_vals = []
            
            if (p_pheno, i + 1) in disease_lut:
                hpo += disease_lut[(p_pheno, i + 1)] 
            else:
                for q_pheno in disease_ith:
                    if (p_pheno, q_pheno) in lut:
                        node_lca = lut[(p_pheno, q_pheno)]
                    else:
                        node_lca = tree_decomp.LCA(p_pheno, q_pheno)
                        lut.update({(p_pheno, q_pheno):node_lca})
                    
                    ic_pq = ic[node_lca - 1]
                    ic_vals.append(ic_pq)
                
                disease_lut.update({(p_pheno, i + 1):max(ic_vals)})
                hpo += max(ic_vals)
            
        hpo_set.append(hpo)
    max_val_hpo = max(hpo_set)
    disease_id = hpo_set.index(max_val_hpo)
    return disease_id + 1


"""
#ic = [2, 4, 6, 42, 8, 10, 18, 16, 12, 22, 24, 20, 26, 14, 28, 34, 30, 36, 38, 40, 32]
#v_id = [1, 2, 3, 3, 5, 2, 3, 5, 1, 1, 8, 10, 9, 11, 15, 13, 15, 15, 16, 15]
#m = 5
#q_set = [[2, 4, 2], [1, 10], [5, 15, 8, 20, 17, 7], [3, 7, 12, 21], [4, 11, 4, 6, 2]] 
#nq = 4
#p_set = [[3, 5, 9, 8], [1, 6], [2, 7, 10], [1, 10]]
ic = [5, 7, 8, 13, 18, 14, 15, 21, 20, 29]
v_id = [1, 1, 3, 3, 4, 4, 5, 5, 5]
m = 2
q_set = [[2, 4, 2], [1, 10]]
nq = 4
p_set = [[3, 5, 9, 8], [1, 5], [2, 8, 10], [1, 10]]

tree = createTree(ic, v_id)
tree_de = Tree_decomp()
tree_de.euler_walk(tree, tree.index, tree.index, 0)
node = tree_de.LCA(4, 9)
lut = {}
disease_lut = {}

for i in range(nq):
    patient_ith = p_set[i][1:]
    
    di_id = func(ic, m, q_set, patient_ith, tree_de, lut, disease_lut)
"""



while(True):
    n_vertices = int(afile.readline())
    v_id = [int(i) for i in afile.readline().rstrip("\r\n").split()]
    ic = [int(i) for i in afile.readline().rstrip("\r\n").split()]
    
    #build tree
    tree = createTree(ic, v_id)
    tree_decomp = Tree_decomp()
    tree_decomp.euler_walk(tree, tree.index, tree.index, 0)
    
    m = int(afile.readline())
    q_set = []
    for i in range(m):
        cm = [int(i) for i in afile.readline().rstrip("\r\n").split()]
        q_set.append(cm)
    
    nq = int(afile.readline())
    p_set = []
    lut = {}
    disease_lut = {}
    count = 0
    
    for i in range(nq):
        cq = [int(i) for i in afile.readline().rstrip("\r\n").split()]
        p_set.append(cq)
        patient_ith = cq[1:]
        disease_id = func(ic, m, q_set, patient_ith, tree_decomp, lut, disease_lut)
        answer_file.write(str(disease_id) + "\n")
        
        
        count += 1
        
        print("{} / {}".format(count, nq))
        
    answer_file.close()
    break
    
afile.close()