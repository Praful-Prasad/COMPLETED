# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 15:24:31 2018

@author: user
"""
import math
print('Quadratic Equation - a*x^2+b*x+c')
a=int(input('Enter value of a - '))
b=int(input('Enter value of b - '))
c=int(input('Enter value of c - '))

var1=((-b)+(math.sqrt(b*b-(4*a*c))))/(2*a)
var2=((-b)-(math.sqrt(b*b-(4*a*c))))/(2*a)
print('Soluions of the quadratic equation are - ',var1,",",var2)