y = input("").split(' ')
y = list(map(int, y))
scores = {

}

for i in range(y[0]):
    scores[i + 1] = 0
lowestrank = {

}
for i in range (y[0]):
    lowestrank[i + 1] = 1
thingy = 0
for i in range(y[1]):
    h = input("").split(" ")
    h = list(map(int, h))
    for i in range(y[0]):
        scores[i + 1] += h[i]
    sortedvalues = (sorted(scores.items(), key=lambda x: x[1], reverse=True))
    for sortedvalue in sortedvalues:
        indexnum = sortedvalues.index(sortedvalue) 
        if thingy < y[0]:
            thingy += 1
            lowestrank[sortedvalue[0]] = indexnum + 1
            print (sortedvalues[indexnum])
        else:
            indexnum = sortedvalues.index(sortedvalue) 
            print (sortedvalue[0])
#maxguy = max(scores)
#print (f"Yodeller {maxguy} is the TopYodeller: score {scores.get(maxguy)}, worst rank ")










