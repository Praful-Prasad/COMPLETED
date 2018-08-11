# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 09:17:36 2018

@author: user
"""

s=input('Enter a string : ')
c=input('Enter a character : ')
for j in range(0,len(s)):
    if(c==s[j]):
        print('Found at index position =',j+1)
        
print("Total number of vowels = ",sum(1 for i in s if i in 'aeiouAEIOU'))
        
        
        
