# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 19:33:45 2018

@author: user
"""

print('Conversions available -')
print('1. kilometre to miles')
print('2. miles to kilometer')
print('3. Celsius to Farenheit')
print('4. Fahrenheit to Celsius')
print('5. Decimal to binary, octal, hexadecimal')

n=int(input('CHOOSE ONE : '))

if(n==1):
    n=int(input('Enter kilometers : '))
    miles=float(0.621371*n)
    print(miles)

if(n==2):
    n=int(input('Enter miles : '))
    kilometres=float(1.60934*n)
    print(kilometres)
    
if(n==3):
     celcius=int(input('Enter celcius : '))
     fh =(celcius*9/5) + 32
     print('Fahrenheit = ',fh)

if(n==4):
    fh=int(input('Enter fahrenheit : '))
    c=(5/9)*(fh-32)
    print('Celsius = ',c)
i=1
octal=0
if(n==5):
    d=int(input('Enter decimal number = '))
    d2=d
    d3=d
    while(d!=0):
        rem=d%8
        octal=octal+(rem*i)
        i=i*10
        d=int(d/8)
    print('Octalnumber = ',octal)
    
    i=1
    octal=0
    while(d2!=0):
        rem=d2%2
        octal=octal+(rem*i)
        i=i*10
        d2=int(d2/2)
       
    print('binarynumber = ',octal)
    i=1
    octal=''
    while(d3!=0):
        rem=d3%16
        if(rem<10):
            octal=str(rem)+octal
            d3=int(d3/16)
        elif(rem==10):
            octal='A'+octal
            d3=int(d3/16)
        elif(rem==11):
            octal='B'+octal  
            d3=int(d3/16)
        elif(rem==12):
            octal='C'+octal+"C" 
            d3=int(d3/16)
        elif(rem==13):
            octal='D'+ octal
            d3=int(d3/16)
        elif(rem==14):
            octal='E'+octal
            d3=int(d3/16)
        elif(rem==15):
            octal='F'+octal
            d3=int(d3/16)
        
    print('hexadecimalnumber = ',octal)
    
    