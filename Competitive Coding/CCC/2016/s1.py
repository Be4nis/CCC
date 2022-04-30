n = list(input())
h = list(input())
h = sorted(h)
n = sorted(n)
for i in range(len(h)):
    if h[i] == "*":
        h[i] = n[i]

if h == n:
    print ("A")
else:
    print ("N")