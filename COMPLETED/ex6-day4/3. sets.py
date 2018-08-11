# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 17:37:49 2018

@author: user
"""

A = {5, 3, 8, 6, 1}
B = {1, 5, 3, 4, 2}

print("union = ",A.union(B))
print("intersection = ",A.intersection(B))
print('Set difference for A = ',A.difference(B))
print('Set difference for B = ',B.difference(A))

print('Max value in A =',max(A))
print('Max value in B =',max(B))

