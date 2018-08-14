# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 10:20:14 2018

@author: user
"""

s=input('Enter a string : ')
a=0
n=0
for i in s:
   
    if(i.isalpha()):
        a=a+1
    elif(i.isnumeric()):
        n=n+1
        
    

print("Total letters = ",a)
print("Total digits = ",n)

