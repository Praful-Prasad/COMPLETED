# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 16:25:00 2018

@author: user
"""

f=open("17.txt","w+")
for i in range(10):
    f.write("line no %d \n"%(i+1)) 
f.close()
f=open("17.txt","r+")
for line in reversed(f.readlines()):
    print(line.rstrip())