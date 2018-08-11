# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:17:34 2018

@author: user
"""

a=input('Enter a string : ')
l=a.split()
l.sort()
print("After sorting words = ")
print(" ".join(l))