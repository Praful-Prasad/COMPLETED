# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 17:32:49 2018

@author: user
"""

f=open("guru99.txt","r+")
for i in range(10):
    f.write("This is line no : %d \n"%(i+1))
for x in f.readlines():
    print(x)
f.close()