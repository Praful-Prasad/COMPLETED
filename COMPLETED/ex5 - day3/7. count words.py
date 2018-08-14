# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 17:57:05 2018

@author: user
"""

f=open("7.txt","w+")
for i in range(10):
    f.write("Line no : %d \n"%(i+1))
f.close()
f=open("7.txt","r+")
sum=0
l=f.readlines()
for x in l:
    str=x.split()
    sum=sum+len(str)
print(sum)
f.close()