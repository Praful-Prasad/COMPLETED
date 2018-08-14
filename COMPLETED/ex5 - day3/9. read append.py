# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 18:13:38 2018

@author: user
"""


f=open("9.txt","w+")
for i in range(10):
    f.write("Line no %d \n"%(i+1))
str=input('Enter a string = ')
f.write(str)

f.close()
f=open("9.txt","r+")
print('New file = ',f.read())
f.close()