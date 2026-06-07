
def Lcm(a,b):
    maxNum=max(a,b)
    print(maxNum)
    while True:
        if(maxNum%a==0 and maxNum%b==0):
            break
        maxNum+=1
        print(maxNum)
    print(f"LCM of {a} and {b} is {maxNum}")             
 
 
Lcm(7,5)    