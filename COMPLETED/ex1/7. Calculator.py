# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:55:51 2018

@author: user
"""


print("\n\n 1. + \t 2. - \t 3. /  \t 4. X")



option=int(input("Select operation(number) : "))
a=int(input("Enter value of A : "))
b=int(input("Enter value of B : "))
if(option==1):
    print("a+b = ",a+b)
elif(option==2):
    print("a-b = ",a-b)
elif(option==3):
    print("a/b = ",a/b)
elif(option==4):
    print("a*b = ",a*b)