class A:
    var1="this is class A"
    
class B:
    var2 = "this is class B"
    
class C(A,B):#multiple inheritance
    var3="this is class C"
    
c1=C()
print(c1.var1)   
    