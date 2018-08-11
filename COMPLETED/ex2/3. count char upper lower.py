# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:35:26 2018

@author: user
"""
a=input('Enter a string : ')
c=0
u=0
l=0
d=0
for x in a:
    if(x.isupper()):
        u=u+1
      
    elif(x.islower()):
        l=l+1
       
    elif(x.isdigit()):
        d=d+1
    c=c+1
print(" No of characters = ",c)

print(" No of upper case characters = ",u)

print(" No of lower case characters = ",l)

print(" No of digits = ",d)
print('Length of string = ',len(a))
d=a+'ing'
print('After adding string = ',d)
b=''
for y in range(0,len(a)):
    if(a[y].isalpha()):
        a=a[0:y+1]+a[y+1:].replace(a[y],'$')
        
        
print('After deleting same occurence of every character = \n',a)