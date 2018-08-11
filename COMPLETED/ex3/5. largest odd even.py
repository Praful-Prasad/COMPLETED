# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:48:38 2018

@author: user
"""

list1=[6541,54,3,4,34,5,6,7,8,243,3,346,36,3,34,78,89]
count=0
n=int(input('Enter the number to search :'))
for i in range(0,len(list1)):
    if(n==list1[i]):
        count=count+1
print(n,' appears ',count,' times')

even=[]
odd=[]
for i in range(0,len(list1)):
    if(list1[i]%2==0):
        even.append(list1[i])
    else:
        odd.append(list1[i])

large=even[0]
for i in range(1,len(even)):
    if(even[i]>large):
        large=even[i]
print('Largest even number = ',large)
small=odd[0]
for i in range(1,len(odd)):
    if(odd[i]<small):
        small=odd[i]
print('Largest odd number = ',small)
    