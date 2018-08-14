# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 18:28:00 2018

@author: user
"""

f=open("11_1.txt","w+")
f.write('First File\n')
f.write('second File\n')
f.write('third File\n')

f.close()
f=open("11_1.txt","r+")
    
f2=open("11_2.txt","w+")
for x in f.readlines():
 
    f2.write(x)
f2.close()

f=open("11_2.txt","r+")
print(f.read())
f.close()