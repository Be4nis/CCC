word = input("")
d = 0
for i in range(0, len(word)+1):
    for s in range(0, len(word)+1):
        p=word[i:s]
        if  p==p[::-1]:
            g = len(p)
            if g>d:
                d =g
print(d)










