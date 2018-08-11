# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 16:50:41 2018

@author: user
"""


d1={'Praful':99,'Monodeep':98,'Ankit':99,'Kuval':80,'Niranjana':70,'Mishra':66,'Manjunath':50,'Jyothi':88,'Nivedita':69,'Akanksha':100}
print(d1)
l=[]
for i in d1.values():
    l.append(int(i))

l.sort()
l2={}
print('Sorted Students list according to marks = \n','Student-Marks')

for x in l:   
    for k,v in d1.items():
        if(v==x):
            l2.update({k:v})

print(l2)