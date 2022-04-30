n = int(input())
s = 0
t = 0
for i in range(n):
    h = list(input())
    for o in h:
        if o == "s" or o == "S":
            s += 1
        if o == "t" or o == "T":
            t += 1

if s == t:
    print ("French")
elif s > t:
    print ("French")
elif t > s:
    print ("English")