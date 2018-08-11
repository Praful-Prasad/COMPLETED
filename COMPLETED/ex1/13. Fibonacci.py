
n=int(input('Enter a number : '))
print("Fibonacci series till n = ")
sum2=0
sum=1
print(0,end=" ")
print(1, end =" ")

for i in range(0,n+1):
    sum3=sum+sum2
    sum2=sum
    sum=sum3
    print(sum,end= " ")
    
    