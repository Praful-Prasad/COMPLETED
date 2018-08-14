# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 18:11:08 2018

@author: user
"""

f=open("8.txt","w+")
for i in range(10):
    f.write("Line no : %d \n"%(i+1))
f.close()
f=open("8.txt","r+")
l=f.readlines()
print(len(l))
f.close()