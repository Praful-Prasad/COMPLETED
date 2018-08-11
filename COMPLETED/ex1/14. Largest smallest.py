# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 19:22:03 2018

@author: user
"""
print('Enter 3 numbers')
a=int(input('Enter a : '))

b=int(input('Enter b : '))

c=int(input('Enter c : '))

if(a>b):
    if(a>c):
        print('a is greatest')
        if(b>c):
            print('c is smallest')
        else:
            print('b is smallest')
    else:
        print('c is greatest') 
        print('b is smallest')
elif(b>c):
    print('b is greatest')
    if(c>a):
        print('a is smallest')
    else:
        print('c is smallest')
else:
    print('c is greatest')
    print('a is smallest')
    