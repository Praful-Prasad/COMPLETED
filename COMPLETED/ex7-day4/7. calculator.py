# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 11:16:07 2018

@author: user
"""
print("1) find the factorial\n2) find LCM\n3) find HCM\n4) factor of a number\n5) Exit\nChoose option")
x=int(input())
def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
while (x!=5):
    if(x==1):
        print(factorial(n))
    elif(x==3):
        a=int(input('Enter a :'))
        b=int(input('Enter b :'))
        if(a<b):
            for i in range(1,a+1):
                if(a%i==0 and b%i==0):
                    hcf=i
        else:
            for i in range(1,b+1):
                if(a%i==0 and b%i==0):
                    hcf=i
                
        print('HCF =',hcf)
    elif(x==2):
        a=int(input('Enter a :'))
        b=int(input('Enter b :'))
        
        j=1
        if(a<b):
            q=b
            lcm=b
            while(lcm%a!=0 or lcm%b!=0):
                b=q*j
                j=j+1
                lcm=b
          
            print(lcm)
    elif(x==4):
        n=int(input('Enter a number : '))
        for i in range(1,n):
            if(n%i==0):
                print("Factor = ",i)
    else:
        print('Wrong input ')