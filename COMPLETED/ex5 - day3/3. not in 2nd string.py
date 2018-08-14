# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 15:51:35 2018

@author: user
"""

s1=set(input('Enter string 1 : '))

s2=set(input('Enter string 2 : '))
print('Uncommon letters in both the strings - ')
x=[print(i) for i in s1 if i not in s2]
