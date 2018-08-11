# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:11:55 2018

@author: user
"""

d1={'Praful':'Prasad','x':'y','z':'a'}
print('Original Dictionary : ',d1)
n=input('Enter a key : ')

if(n in d1):
    print(n,':',d1[n])
else:
    print('Not found')