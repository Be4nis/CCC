i = int(input())
k = []
def split(word):
    return [char for char in word]
for h in range(i):
    p = list(input())
    while "-" in p:
        p.remove("-")
    k.append(p)

print (k)