# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 15:47:19 2018

@author: user
"""

s1=set(input('Enter string 1 : '))

s2=set(input('Enter string 2 : '))
count=0
print('Common letters in both the strings are - ',)
x=[print(i) for i in s1 if i in s2]
