#print positive and negative numbers from the list  

a=[10, 20, 30, -40, -50, -60, 70, -80, 90, -100]



print("positive numbers are: ")
for i in a:
    if i>0:
        print(i)

print("negative numbers are: ")
for i in a:
    if i<0:
        print(i)        