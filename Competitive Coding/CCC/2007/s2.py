def flatten(t):
    return [item for sublist in t for item in sublist]

n = int(input(""))


dimensions = []
packagesizes = []

for y in range(n):
    i = input("").split(' ')
    p = list(map(int, i))
    tempvar = 1
    dimensions.append(p)
    for h in range(len(p)):
        tempvar = p[h] * tempvar
    packagesizes.append(tempvar)
packagesizes = list(set(packagesizes))

packagesizes.sort()
numofpack = int(input(""))
packs = []


for y in range(numofpack):
    i = input("").split(' ')
    p = list(map(int, i))
    tempvar = 1
    t = 0
    if max(p) > max(flatten(dimensions)):
        tempvar = 100000
    for h in range(len(p)):
            tempvar = p[h] * tempvar 
    packs.append(tempvar)



final = []
numbers = []
for pack in packs:
    tempvar = 0
    for packagesize in packagesizes:
        if pack == packagesize and tempvar == 0:
            tempvar += 1
            final.append(packagesize)
            numbers.append(pack)
        elif pack < packagesize and tempvar == 0:
            tempvar += 1
            final.append(packagesize)
            numbers.append(pack)
        elif pack > max(packagesizes) and tempvar == 0:
            tempvar += 1
            final.append('Item does not fit.')

for f in final:
    print (f)


