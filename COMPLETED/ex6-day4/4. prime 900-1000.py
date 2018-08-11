# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 09:39:38 2018

@author: user
"""
flag=0
l=[]
for i in range(900,1001):
    for j in range(2,i):
        if(i%j==0):
            flag=1
    if(flag==0):
        l.append(i)
    flag=0
    a=str(i)
    if(a[::-1]==str(i)):
        print('Palindrome found = ',a)
        
for x in l:
    print("Prime numer found = ",x)
    
