# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 15:06:23 2018

@author: user
"""
import collections
import numpy
a="#Python is an interpreted high level programming language for general-purpose programming*"
b=''

for x in a:
    if(x.isalnum() or x==' '):
        b=b+x
print("\n\nAfter removing Special characters=",b)

for x in b.split():
    if(x==x[::-1]):
      print('\n',x,"is a palindrome")
      
print("Repeating words = \n")

for k,v in (collections.Counter(b.split()).items()):
    if(v>1):
        print(k,' : ',v)

w=collections.Counter(b.split())
print()