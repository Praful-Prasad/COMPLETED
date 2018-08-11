# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:31:52 2018

@author: user
"""
import math
l=[1,2,3,4,5,6,7,8,9,10,25,36,81,169]
for i in range(0,len(l)):
    if(math.sqrt(l[i]).is_integer()):
        n=l[i]
        sum=0
        while(n>0):
            d=n%10
            sum=sum+d
            n=int(n/10)
        if(sum<10):
            print(l[i])