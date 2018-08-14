# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 12:51:01 2018

@author: user
"""

f=open("16.txt","w+")
for i in range(10):
    f.write("line no %d \n"%(i+1)) 
f.close()

f=open("16.txt","r+")

print('----')
f2=open("16_2.txt","w+")
total_lines=f.readlines()
for single_line in total_lines:
    list_of_words_single_line = single_line.split()
    for single_word in list_of_words_single_line:
        for i in range(len(single_word)):
            if(i==0):
                z=single_word[i].upper()
            else:
                z=z+single_word[i]
        f2.write(z)
        f2.write(' ')
    f2.write('\n')
f2.close()
f.close()
f2=open("16_2.txt","r+")
print(f2.read())
f.close()