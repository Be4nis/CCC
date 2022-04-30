#50/90 Points, not all
n = int(input())

specs = {

}

for i in range(n):
    h = input()
    h = h.split(' ')
    if n == 1:
        print (h[0])
    else:
        one = int(h[1])
        two = int(h[2])
        three = int(h[3])
        n = (2*one + 3*two + three)
        specs[h[0]] = n
    
highest = max(specs, key=specs.get)

max = max(specs.values())
max2 = 0
for v in specs.values():
    if(v>max2 and v<max):
            max2 = v

keylist = list(specs.keys())
vallist = list(specs.values())

position = vallist.index(max2)
#max2 is value of second highest
#max1 is value of highest
max1 = specs[highest]

print (highest)
print (keylist[position])








