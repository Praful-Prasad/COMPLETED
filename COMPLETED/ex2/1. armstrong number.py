# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

n=int(input('Enter a number : '))
sum=0
n2=n
length=len(str(n))

while n>0:
    rem=n%10
    sum=sum+math.pow(rem,length)
    n=int(n/10)
    
if(sum==n2):
    print('Its an armstrong number')
else:
    print('Its not')
    