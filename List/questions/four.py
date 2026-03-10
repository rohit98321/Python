#find the second greatest and element

a=[1,22,3,4,5]

max=0
second=0

for i in a:
    if i>max:
        second=max
        max=i



print(f"second greatest is {second}")        

