# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 18:16:40 2018

@author: user
"""

string= input('Enter a string : ')
l1=[]
l1=string.split()
l2=[]
for i in range(0,len(l1)):
    n=l1.count(l1[i])
    l2.append(n)
df=dict(zip(l1,l2))
print(df)