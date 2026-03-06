#print any table through the input

a=int(input("Enter the table no for print: "))

for i in range(a,(a*10+1),a):
    print(f"{a} x {i//a} = {a*(i//a)}")