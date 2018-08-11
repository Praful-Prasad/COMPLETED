# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 14:56:32 2018

@author: user
"""

from numpy import *

a = array([['Rhia',10,20,30,40,50],
           ['Alan',75,80,75,85,100],
           ['Smith',80,80,80,90,95]])


print(a[:3,:2])
a[2]=['Sam',82,79,88,97,99]
print('After adding = \n',a)
a[0][3]=95
print('After editing = \n',a)
a= insert(a,[6],[[73],[80],[85]],axis=1)
print('After appending :\n ',a)
