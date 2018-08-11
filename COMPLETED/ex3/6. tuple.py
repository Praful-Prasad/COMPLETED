# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:58:17 2018

@author: user
"""
n=0
l=[]


while(n!=-1):
    n=int(input('Enter a number (Enter -1 to end) :'))
    if(n!=-1):
        t=(n,n*n)
        l.append(t)

print('Final list with tuples = ',l)
l.sort()
print('After sorting = ',l)