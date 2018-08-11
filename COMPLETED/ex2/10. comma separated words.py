# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 09:28:39 2018

@author: user
"""

s=input('Enter a string (comma separated ):')
s=s.split(",")
s.sort()
print('Sorted words = ',",".join(s))