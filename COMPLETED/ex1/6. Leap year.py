# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 18:52:10 2018

@author: user
"""

a=int(input('Enter year : '))
if(a%400==0):
    print('It is a leap year')
elif(a%100==0):
    print('Not a leap year')
elif(a%4==0):
    print('This is a leap year')