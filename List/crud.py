a=[10,20,30,40,50,60,70,80,90,100]

a.append(110)
a.insert(0,55)
a.remove(20)


for i in range(len(a)):
    print(a[i])

a.extend([120,130])

print("After extend")

for i in a: print(i)
