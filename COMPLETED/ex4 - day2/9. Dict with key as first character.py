# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 16:46:35 2018

@author: user
"""

test=input("Enter string:")
l=test.split()
d={}
for word in l:
    if(word[0] not in d.keys()):
        d[word[0]]=[]
        d[word[0]].append(word)
    else:
        if(word not in d[word[0]]):
          d[word[0]].append(word)
for k,v in d.items():
        print(k,":",v)