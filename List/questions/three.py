#find the greatest and index too


a=[1,22,3,4,5]

max=0
index=0

for i in range(len(a)):

    if a[i]>max:
        max=a[i]
        index=i

print(f"max is {max} and index is {index+1}")        

