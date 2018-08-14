# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 18:16:59 2018

@author: user
"""
import collections 
f=open("10.txt","w+")
l=[]
for i in range(10):
    f.write("Line no %d \n"%(i+1))
f.close()
f=open("10.txt","r+")
for x in f.readlines():
    l=l+x.split()
print(collections.Counter(l))
f.close()
