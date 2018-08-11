4# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:23:46 2018

@author: user
"""

import numpy as np
n=0
l=[]
while (n!=-1):
    n=int(input('Enter coefficients of the polynomial = '))
    if(n!=-1):
        l.append(n)

print(l)
l.sort()
print(np.roots(l))