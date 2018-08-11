# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:54:56 2018

@author: user
"""


a=input('Enter a string : ')
l=list(a)
temp=l[0]
l[0]=l[-1]
l[-1]=temp
print("Reversin first and last element = ")

print("".join(l))
