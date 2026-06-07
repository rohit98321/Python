str="clotriwal"
freq={}

for ch in str:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)

for key,value in freq.items():
    print(f"{key} : {value}")