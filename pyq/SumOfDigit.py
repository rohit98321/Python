a=int(input("enter a number: "))

sum=0
while a > 0:
    
    rem=a%10
    sum+=rem
    a=a//10
print(f"sum of digit is {sum}")