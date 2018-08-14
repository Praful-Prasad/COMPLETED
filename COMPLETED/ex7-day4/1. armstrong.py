# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
for n in range(1,1001):
    sum=0
    n2=n
    length=len(str(n))

    while n>0:
        rem=n%10
        sum=sum+math.pow(rem,length)
        n=int(n/10)
    
    if(sum==n2):
        print(n2,' is an armstrong number'  )
  
    