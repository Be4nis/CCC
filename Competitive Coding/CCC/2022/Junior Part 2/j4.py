x = int(input(""))
samegroup = []

for i in range(x):
    names = input("").split(' ')
    samegroup.append(names)

y = int(input(""))
diffgroup = []

for i in range(y):
    names = input("").split(' ')
    diffgroup.append(names)

g = int(input(""))

violations = 0

for i in range(g):
    names = input("").split(' ')
    for same in samegroup:
        if (same[0] in names) and (same[1] not in names):
            violations += 1
    for diff in diffgroup:
        if (diff[0] in names) and (diff[1] in names):
            violations += 1
print (violations)