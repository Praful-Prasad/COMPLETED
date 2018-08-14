# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 10:05:49 2018

@author: user
"""

import numpy as np
A =[[3, 5, 6],[4, 8, 10],[2, 1, 8]] 
I = [[1, 0, 0],[0, 1, 0],[0, 0, 1]]
B=np.dot(A,I)
if(np.array_equal(A,B)):
    print("A.I = ",np.dot(A,I)," \nHence Proved")