import math
list1=[1,8,3,7,3,3,2,5,4,3,435,3]
list2=[8,7,6,9,8,456,45,3]
print('list1 = ',list1)
print('list2 = ',list2)

list3=list(set(list1).union(set(list2)))

print('Union of two lists = ',list3)

print('Intersection of lists = ',set(list1) & set(list2))