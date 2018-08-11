# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 15:15:07 2018

@author: user
"""
x=int(input('Enter a number :'))
flag=0
for n in range(2,x):
    if(x%n==0):
        flag=1;

if(flag==1):
    print('Number is not prime')
else:
    print('Number is prime')