# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 18:37:38 2018

@author: user
"""

f=open("12.txt","w+")
f.write('First Line\n')
f.write('second Line\n')
f.write('third Line\n')
f.close()
f=open("12.txt","r+")
l=[]
c=input('Enter character to search : ')
count=0
for x in f.read():
    if(c==x):
        count=count+1
        l=l+list(x)
print(count)

f.close()