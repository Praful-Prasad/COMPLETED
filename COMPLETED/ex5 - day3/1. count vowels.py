# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 15:42:38 2018

@author: user
"""

s=input('Enter a string : ')
vowels=set("aeiouAEIOU")
count=0
for i in range(len(s)):
    if(s[i] in vowels):
        count=count+1

print('Total number of vowels = ',count)