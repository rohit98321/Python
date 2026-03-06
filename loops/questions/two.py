#sum of digits

a=int(input("Enter the number: "))

sum=0
while a>0:
    remainder=a%10
    sum+=remainder
    a=a//10


    
    print(sum)
