# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 18:25:28 2018

@author: user
"""
n=int(input('Enter a number : '))
def fact(x):
    if(x==0):
        return 1
    return x*fact(x-1)

print(fact(n))


def fibo(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
print('Fibonacci sum =',fibo(n))
