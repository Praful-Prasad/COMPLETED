# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 12:54:46 2018

@author: user
"""

list1=[1,3,4,5,7,5,4,7,7,0]
print('Original List = ',list1)
large = list1[0]
large2=list1[1]
small=list1[0]
for i in range(1,7):
    if(list1[i]>large):
        large2=large
        large=list1[i]
        
        l=i
    elif(list1[i]<small):
        small=list1[i]

print ('Largest number is : ', large)

print ('Second largest number is : ', large2)

temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp

print ('After swapping :',list1)