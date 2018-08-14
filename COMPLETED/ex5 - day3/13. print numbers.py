# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 18:55:06 2018

@author: user
"""


f=open("13.txt","w+")
f.write('1 Line\n')
f.write('2 Line\n')
f.write('3 Line\n')
f.close()
f=open("13.txt","r+")

count=0
for x in f.read():
    if(x.isnumeric()):
        print(x)


f.close()