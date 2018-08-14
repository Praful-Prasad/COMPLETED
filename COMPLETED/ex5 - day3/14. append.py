# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 18:57:57 2018

@author: user
"""


f=open("14_1.txt","w+")
f.write('First File\n')
f.write('second File\n')
f.write('third File\n')

f.close()
f2=open("14_2.txt","w+")
f=open("14_1.txt","r+")
f2.write('fourth File\n')
f2.write('fifth File\n')
f2.write('sixth File\n')
f2.close()
f2=open("14_2.txt","a+")
for x in f.readlines():
    f2.write(x)
f2.close()
f2=open("14_2.txt","r+")

print(f2.read())
f2.close()
f2.close()