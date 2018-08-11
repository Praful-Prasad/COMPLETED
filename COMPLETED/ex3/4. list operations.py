# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:44:37 2018

@author: user
"""

list1=[1,2,3,4,5,6,7,8]
print('3rd element = ',list1[2],' 6th element = ',list1[5])
for i in range(0,5):
    print(list1[i])
print('7th element from end = ',list1[-7])
list1[1]='x'
list1[4]='y'
print('After changing 2nd and 5th element by x and y respectively',list1)
del list1[4]

print('After removing 5th element resulting list =',list1)
print("Total number of elements = ",len(list1)," list = ",list1)

