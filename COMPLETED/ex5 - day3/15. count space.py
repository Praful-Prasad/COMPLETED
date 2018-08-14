# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 11:11:15 2018

@author: user
"""



f=open("15.txt","w+")

for i in range(10):
    f.write("Line no %d \n"%(i+1))
f.close()
f=open("15.txt","r+")
count=0
for x in f.read():
    if(x==' '):
        count=count+1
print('Total numer of spaces = ', count)
f.close()

