k = int(input())
g1s = input()
g1s = g1s.split(' ')
g2s = input()
g2s = g2s.split(' ')

i = 0
goodorbad = "good"
while i < k and goodorbad == "good":
    position = g1s.index(g2s[i])
    if g1s[i] != g2s[position] or position == i:
        goodorbad = "bad"
    i += 1
    
print (goodorbad)
