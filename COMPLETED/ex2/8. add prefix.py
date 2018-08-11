# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 18:35:48 2018

@author: user
"""

l=[]
x=input('Enter strings ...enter "x" to exit.\n')
while(x!='x'):
    l.append(x)
    x=input()
    
prefix=input('Enter prefix text to add : ')
w=""
for x in range(0,len(l)):
    w=prefix+l[x]
    l[x]=w
for x in l:
    print(x)