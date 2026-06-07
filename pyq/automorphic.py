n=int(input("enter the number to check :  "))

def lastdigit(n):
    rem=n%10
    return rem;
 
def automorphic(n):
    sq=n*n
    a=lastdigit(sq)
    b=lastdigit(n)
    if a==b:
        print("yes")
    else:
        print("no")    
    
    
 
automorphic(n)
 