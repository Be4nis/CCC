street = 1000000
def hydrants(hose, houses):
    best = len(houses)
    diam = hose * 2
    
    i = 0
    while i < len(houses) and houses[i] <= houses[0] + diam:
        count = 1
        curEnd = houses[i]
        j = i + 1
        while j < len(houses) and (houses[i] > (houses[j] + diam - street)):
            if houses[j] > curEnd:
                count += 1
                curEnd = houses[j] + diam
            j = j + 1
        best = min(best, count)
        i = i + 1
    return best

h = int(input(""))
houses = []
for i in range(h):
    p = int(input(""))
    houses.append(p)
houses.sort()
k = int(input()) 
lo = -1
y = street
while (y > (lo+1)):
    mid = (lo + y) // 2
    if (hydrants(mid, houses) > k):
        lo = mid
    else:
        y = mid
print (y)